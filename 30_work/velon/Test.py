# -*- coding: utf-8 -*-
import datetime

from dict import MysqlMetaHandler
from dict.AbstractMetaHandler import SrcTableDict
from util import MysqlUtil, MysqlPoolUtil
from util.IdWorker import IdWorker

if __name__ == '__main__':
    # ====================源端连接信息===============================

    # 获取源端数据库链接
    def conGet():
        connLinkList = MysqlUtil.query(
            "SELECT domain,company_code,conn_command  FROM `src_connect_info` ORDER BY company_code ")
        conDic = {}
        if (connLinkList):
            for con in connLinkList:
                conDic[con[0] + "_" + con[1]] = con[2]

        print(conDic)


    # conGet()

    def conGetWhere():
        company_code = '00';
        domain = 'xt'
        connLinkList = MysqlUtil.query(
            "SELECT host,username,password,port,db_name  FROM `src_connect_info` where db_type= 'mysql' and company_code= '%s' and domain = '%s' " % (
                company_code, domain
            ))

        conDic = {}
        # if (connLinkList):
        #     for con in connLinkList:
        #         conDic[con[0] + "_" + con[1]] = con[2]

        if (connLinkList):
            print(connLinkList[0])

        # print(conDic)


    # conGetWhere()

    # ====================表信息===============================

    # 获取表的注释信息 和列信息拼接
    def sourDataGetTableCommet(schema, tablename):
        tableList = MysqlUtil.query(
            " SELECT  *  FROM information_schema.tables WHERE table_schema ='%s'  AND table_name = '%s' " % (
                schema, tablename))
        if (tableList):
            # for table in tableList:
            #     print(table)
            print(tableList[0])
            print(tableList[0][20])


# TODO 某些表获取不到信息
# print("表信息")
# sourDataGetTableCommet("csg_info", "des_table_extra_info")
# sourDataGetTableCommet("csg_info", "src_table_dict_03_yx")
# sourDataGetTableCommet("csg_info", "src_table_dict_test")
# sourDataGetTableCommet("csg_info", "info_des_table_view")


# =====================列信息==============================


# 根据schema/表名 从information_schema.columns 获取单张表cols信息
# 规定返回对象list,避免达梦/Oracle/MySQL不同数据库返回数据不一致

# 遍历对象
# for line in sourColsGetPojo("csg_info", "src_table_extra_info"):
#     # print(line)
#     for attr, value in line.__dict__.items():
#         print(attr, value)
#
#     print("====")


# ------------------返回元组------------------------------
# 获取源端列数据 返回元组list
def sourDataGet(schema, tablename):
    # 返回对象list
    colslistRes = list();
    colsList = MysqlUtil.query(
        " SELECT  *  FROM information_schema.columns WHERE table_schema ='%s'  AND table_name = '%s' " % (
            schema, tablename))
    if (colsList):
        for conlItem in colsList:
            # print(conlItem[0])
            colslistRes.append(conlItem)
    return colslistRes


# for line in sourDataGet("csg_info", "src_table_extra_info"):
#     # print(line)
#     # print(line.list())
#     print(line[5])
#     print("====")

# ===================写数据到MySQL================================


# IF( '%s'='None','%s',null)
# IF( '%s'='None','%s',null)

def insSql(conls):
    insertSql = """insert into csg_info.src_table_dic_test (
                        domain
                        ,company_code
                        ,sys_name
                        ,table_schema
                        ,table_name
                        
                        ,table_name_zh
                        ,column_position
                        ,column_name
                        ,pk
                        ,data_type
                        
                        ,data_length
                        ,data_precision
                        ,data_scale
                        ,data_default
                        ,nullable
                        
                        ,table_comment
                        ,column_comment
                        ,remark 
                        ,table_name_des
                         )         
                   values  ( '%s','%s','%s' ,'%s' ,'%s', 
                             '%s','%s','%s' ,'%s' ,'%s', 
                             '%s','%s','%s' ,'%s' ,'%s', 
                             '%s','%s','%s' ,'%s' 
                            ) """ % (
        conls.get_domain()
        , conls.get_company_code()
        , conls.get_sys_name()
        , conls.get_table_schema()
        , conls.get_table_name()

        , conls.get_table_name_zh()
        , conls.get_column_position()
        , conls.get_column_name()
        , conls.get_pk()
        , conls.get_data_type()

        , conls.get_data_length()
        , conls.get_data_precision()
        , conls.get_data_scale()
        , conls.get_data_default()
        , conls.get_nullable()

        , conls.get_table_comment()
        , conls.get_column_comment()
        , conls.get_remark()
        , conls.get_table_name_des()

    )
    MysqlUtil.upsert(insertSql)


# ------单条数据写入 测试-------------------



# ------批量数据写入 测试-------------------
#

# ================= 连接池测试======================

def poolTest():
    host = '10.92.172.50'
    port = 20015
    username = 'deltalake'
    password = 'Deltalake..172'
    db = 'csg_info'
    charset = 'utf8'

    pool = MysqlPoolUtil.pool(host, username, password, port, db)

    MysqlPoolUtil.query(pool,
                        " SELECT host,username,password,port,db_name  FROM `src_connect_info` where db_type= 'mysql' and company_code= '13' and domain = 'local'  ")


# poolTest()


# ================= MysqlMetaHandler 测试======================

def mysqlHandlerTest():
    item = list()

    # table_id
    item[0] = '11111'
    # company_code
    item[1] = '99'
    # domain
    item[2] = 'local'
    # table_schema
    item[3] = 'csg_info'
    # table_name
    item[4] = 'src_table_extra_info'
    # db_type
    item[5] = 'mysql'
    # table_name_des\
    item[6] = ''

    print(item)

    # MysqlMetaHandler.handle(item)
