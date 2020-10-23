import os
import yarn
import subprocess
import time
import json
import argparse

from util import MysqlUtil,ImpalaUtil,OracleUtil
from conf import config, log
import pyhdfs
import statistic


def writerError(logger,table_id,table_full_name,writer_name,msg,path):
    statistic.failure += 1
    log.logger.error(msg)
    logger.error("tableId:%d,tableName:%s,msg:%s" % (table_id,table_full_name,msg))
    if(writer_name=="kuduwriter"):
        MysqlUtil.upsert("update des_table_extra_info set state=0,error='%s',data_oper_time=now() where table_id=%d" % (msg,table_id))
    else:
        MysqlUtil.upsert("update src_table_extra_info set state=0,error='%s',data_oper_time=now() where table_id=%d" % (msg, table_id))
    #subprocess.getstatusoutput("mv " + path + " " + path + ".success")

def call(mode, yarn_name, path,version=-1):

    if(not str(path).endswith(".json")):
        log.logger.warn("not json file,skip:" + path)
        statistic.skip+=1
        return

    statistic.processing+=1

    log.logger.debug("json file:" + path)
    json_file = json.load(open(path, encoding='utf-8'))
    job = json_file['job']
    info = json_file['info']
    pk_cols = info['pkCols']
    table_id=info['tableId']
    company_code = info['companyCode']
    domain = info['domain']
    table_schema = info['tableSchema']
    table_name = info['tableName']

    rows=info['rows']
    table_full_name=table_schema+"."+table_name
    content = job['content'][0]
    reader = content['reader']
    writer = content['writer']
    reader_name = str(reader['name']).lower()
    writer_name = str(writer['name']).lower()

    #日志输出目录
    log_dir=os.path.join(config.flinkx_log_dir,company_code)
    success_logger= log.getFileLogger(company_code+"_"+domain+"_success",log_dir)
    failure_logger = log.getFileLogger(company_code + "_" +domain+"_failure",log_dir)


    if(statistic.company_code==None and statistic.domain==None):
        statistic.company_code=company_code
        statistic.domain=domain

    if (writer_name=="kuduwriter"):
        if(not pk_cols):
            log.logger.warn("this table has not primary key,skip:" + path)
            statistic.nopk+=1
            return

        if(int(rows)<=0):
            log.logger.warn("this table has no record,skip:" + path)
            statistic.empty += 1
            return

        # 根据mysql中的ddl创建kudu表
        sql = "SELECT cdh%s_impala_ddl FROM des_table_info t1 JOIN des_table_extra_info t2 ON  t1.table_id=t2.table_id WHERE company_code='%s' AND domain='%s' AND table_schema='%s' AND table_name='%s'" % (
        config.cdh_version, company_code, domain, table_schema, table_name)
        result = MysqlUtil.query(sql)
        if (result):
            ddl = result[0][0]
            statusoutput = ImpalaUtil.shell(ddl)
            status = statusoutput[0]
            if (status != 0):
                msg = "impala create table error:" + str(ddl)
                writerError(failure_logger, table_id, table_full_name, writer_name, msg, path)
                return
        else:
            msg = "can not found the kudu ddl in mysql"
            writerError(failure_logger, table_id, table_full_name, writer_name, msg, path)
            return



    items = config.app[company_code + "-" + domain]
    username = items['username']
    password = str(items['password'])
    sql = 'SELECT count(*) from ' + table_full_name

    src_count = rows
    src_size = -1

    # 检查hdfs路径是否存在
    if (reader_name == "hdfsreader"):
        hdfs_path = reader['parameter']['path']
        hdfs_path = hdfs_path[hdfs_path.find("//") + 2:]
        hdfs_path = hdfs_path[hdfs_path.find("/"):]
        client = pyhdfs.HdfsClient(hosts=config.hdfs_http_url, user_name=config.hdfs_user_name)
        if (not client.exists(hdfs_path)):
            msg="hdfsreader can not find the data path," + hdfs_path
            writerError(failure_logger,table_id,table_full_name,writer_name,msg,path)
            return
        else:
            log.logger.debug("[check hdfs path exist: " + str(client.exists(hdfs_path)) + ']')
    pass

    if(reader_name == "oraclereader"):
        dsn = str(items['jdbcUrl']).replace('jdbc:oracle:thin:@', '')
        pool=OracleUtil.pool(dsn, username, password)
        result=OracleUtil.query(pool, sql)
        if(result):
            src_count=int(result[0][0])
            log.logger.info("Query Rows Result:"+str(src_count))
        else:
            msg = "Oracle Query Rows Error:Can Not Find The Record"
            writerError(failure_logger,table_id,table_full_name,writer_name,msg,path)
            return
    pass

    if (reader_name == "dmreader"):
        dsn = str(items['jdbcUrl']).replace('jdbc:dm://', '')
        cmd="disql %s/%s@%s -e '%s'" % (username,password,dsn,sql)  #查询表记录数
        sql2="select table_used_pages('%s','%s')*(page()/1024)/1024 from dual" % (table_schema.upper() ,table_name.upper())
        cmd2="disql %s/%s@%s -e \"%s\"" % (username,password,dsn,sql2)  #查询表大小
        log.logger.info("Query Rows:"+cmd)
        status=subprocess.getstatusoutput(cmd)
        if(status[0]!=0):
            msg="dm can not query the rows number:"+cmd
            writerError(failure_logger,table_id,table_full_name,writer_name,msg,path)
            return
        else:
            output=status[1].split('\n')
            src_count=int(output[len(output)-1])
            log.logger.info("Query Rows Result:"+str(src_count))
            pass

        log.logger.info("Query Size:" + cmd2)
        status = subprocess.getstatusoutput(cmd2)
        if (status[0] != 0):
            msg = "dm can not query the rows size:" + cmd
            writerError(failure_logger, table_id, table_full_name, writer_name,msg,path)
            return
        else:
            output = status[1].split('\n')
            src_size= float(output[len(output)-1])
            log.logger.info("Query Size Result:" + str(src_size))
        pass

        #从达梦库上获取到的rows和size，更新到mysql中，这段逻辑以后要删除
        sql = "update src_table_extra_info set `rows`=%d,`size`=%.2f where table_id=%d" % (src_count, src_size, table_id)
        MysqlUtil.upsert(sql)
    pass




    #并接执行命令
    log.logger.info("####################  call flinkx start #########################")
    cmd = "{flinkx_cmd_path} {mode} {yarn_name} {path} ".format(flinkx_cmd_path=config.flinkx_cmd_path, mode=mode,yarn_name=yarn_name,path=path)
    log.logger.info(cmd)
    #调用
    statusoutput=subprocess.getstatusoutput(cmd)
    status=statusoutput[0]
    output = statusoutput[1]
    #输出每个表的日志
    table_logger=log.getFileLogger(table_full_name,log_dir)
    table_logger.info(output)
    #命令执行状态
    if(status!=0): #出错
        msg="flinkx call error,see the flinkx log"
        writerError(failure_logger, table_id, table_full_name, writer_name,msg,path)
        return
    else:
        #status==0，成功
        logs = output.split("\n")
        log_len = len(logs)

    des_count=None
    if mode == "local":
        num_write = int(logs[log_len-15].split("|")[1])
        des_count=num_write
        null_errors = int(logs[log_len-3].split("|")[1])
        n_errors = int(logs[log_len - 2].split("|")[1])
        if(null_errors > 0 or n_errors > 0 ):
            msg = "flinkx import error,the number of error records is %d" % (null_errors+n_errors)
            writerError(failure_logger, table_id, table_full_name, writer_name,msg,path)
            return
        pass

    elif mode == "yarnPer":
        #读取日志文件获取applicationId
        last_row = logs[log_len - 1]
        application_id = last_row[last_row.find("appId: ")+6:last_row.find("},")]
        log.logger.debug("yarn_application_id:"+application_id.strip())
        #根据applicationId调用yarn获取状态

        while True:
            state = yarn.get_state(application_id.strip())
            log.logger.debug("check yarn state:"+state)
            if(state=="FINISHED" or state=="FAILED" or state=="KILLED"):
                break
            time.sleep(15)     #休眠15秒

    log.logger.info("####################  call flinkx end #########################")

    if(writer_name=="kuduwriter"):
        #查询impala
        log.logger.debug("##################     impala  info     ############################")
        impala_sql = "select count(1) from csg_ods_{company_code}_{domain}.{table_name}".format(company_code=company_code, domain=domain, table_name=table_name)
        statusoutput = ImpalaUtil.shell(impala_sql)
        status = statusoutput[0]
        output = statusoutput[1]
        if (status != 0):
            msg="impala query count error"
            writerError(failure_logger, table_id, table_full_name, writer_name,msg,path)
            return
        #输出记录数
        logs = output.split("\n")
        des_count = int(logs[len(logs) - 2])
        log.logger.debug("des count:"+str(des_count))
    pass

    if (src_count == des_count):
        log.logger.info("##########################  success info  ###########################")
        msg = "count:"+str(src_count)
        success_logger.info("tableId:%d,tableName:%s,msg:%s" % (table_id,table_full_name,msg))
        #如果是消费消息队列，则会传入version,如果不是，直接更新数据库中的版本
        if(version==-1):
            data_version="data_version+1"
        else:
            data_version=str(version)

        if(writer_name=="kuduwriter"):
            MysqlUtil.upsert("update des_table_extra_info set state=1,error=null,data_oper_time=now(),data_version=%s where table_id=%d" % (data_version,table_id))
        elif(writer_name=="hdfswriter"):
            hdfs_path=writer['parameter']['path']
            MysqlUtil.upsert("update src_table_extra_info set state=1,error=null,data_oper_time=now(),data_version=%s,hdfs_path='%s' where table_id=%d" % (data_version,hdfs_path,table_id))
        else:
            MysqlUtil.upsert("update src_table_extra_info set state=1,error=null,data_oper_time=now(),data_version=%s where table_id=%d" % (data_version,table_id))
        statistic.success+=1
        cmd="mv "+path+" "+path+".success"
        log.logger.info(cmd)
        subprocess.getstatusoutput(cmd)

    else:
        log.logger.info("##########################  failure info  ###########################")
        msg = "number is not match,src number:%d,des number:%d"% (src_count,des_count)
        writerError(failure_logger, table_id, table_full_name, writer_name,msg,path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='launcher...')
    parser.add_argument("--mode", type=str, default="local")
    parser.add_argument("--json", type=str)
    parser.add_argument("--name", type=str, default='flink')
    args = parser.parse_args()
    call(args.mode, args.name, args.json)
    pass