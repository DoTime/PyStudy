import subprocess as sub
import argparse


# 问题:
# 源表无表: 返回提示


# 表是否存在 是1 否0
def exitTab(sqlBase, db, tab):
    sql = "  SELECT COUNT(1) as cnt FROM pg_class c LEFT JOIN pg_namespace n ON (n.oid = c.relnamespace) WHERE n.nspname = '%s' AND c.relname = '%s' \" " % (db, tab)
    return sub.run(sqlBase + sql, shell=True)
    # return 1


# 为用户授权
def grantUse(sqlBase, db, tab, user):
    db_table = db + "." + tab

    g1 = "grant select on %s to %s  " % (db_table, user)
    g2 = "grant usage on schema dwzc to %s  " % (user)
    # df_00_sjgcxm  父权限 固定值
    g3 = "grant df_00_sjgcxm to %s " % (user)
    print()
    print(sqlBase + g1 + "\"")
    print(sqlBase + g2 + "\"")
    print(sqlBase + g3 + "\"")
    sub.run(sqlBase + g1 + "\"", shell=True)
    sub.run(sqlBase + g2 + "\"", shell=True)
    sub.run(sqlBase + g3 + "\"", shell=True)


# 表存在 > 判断表是否是分区表 是t  否 f
# select relhassubclass from  pg_class
def isParTab(db, tab):
    sql = " SELECT c.relhassubclass FROM pg_class c LEFT JOIN pg_namespace n ON (n.oid = c.relnamespace) WHERE n.nspname = '%s' AND c.relname = '%s' \" " % (db, tab)
    return sub.run(sqlBase_ori + sql, shell=True)


# 表数据量  psql -h 10.91.23.186 "dbname=kaifa_37 user=gpadmin password=gpadmin" -c "select count(1) from  dwzc.twb_m_sp_pd_fault_report"
def couTab(sqlBase, db, tab):
    sql = " select count(1) from  %s   \" " % (db + "." + tab)
    return sub.run(sqlBase + sql, shell=True)
    # return 0


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='launcher...')

    parser.add_argument("--oriIP", type=str, default="127.0.0.37")
    parser.add_argument("--dbname", type=str, default="dbn")
    parser.add_argument("--tabname", type=str, default="tabname")

    parser.add_argument("--code", type=str, default="02")
    parser.add_argument("--where", type=str, default="where 1=1")
    parser.add_argument("--username", type=str, default="gpuser")

    args = parser.parse_args()

    oriIP = args.oriIP
    dbname = args.dbname
    tabname = args.tabname

    code = args.code
    where = args.where
    username = args.username

    db_table = dbname + "." + tabname

    # 源库ip   目标库模式.目标库表名    分省代码   where条件  用户名
    # --oriIP=127.0.0.37 --dbname=dbn --tabname=table2233 --code=03 --where="where 1=1" --username=uname

    print("=======args==========")
    print(args)

    # 源端连接   >分别连接5个集群  参数:10.92.208.37
    sqlBase_ori = "psql -h %s -p 5432 -U gpadmin -d csgbi " % (oriIP)
    dbip = oriIP.split('.')[3]  # 37 38

    # 目标端 dbname=kaifa_37  37为参数
    # 目标  测试/开发环境   psql -h 10.91.23.186 "dbname=ceshi_37 user=gpadmin password=gpadmin"  -t  -c
    sqlBase_cs = """ psql -h 10.91.23.186 "dbname=ceshi_%s user=gpadmin password=gpadmin"  -t  -c \"  """ % (dbip)
    sqlBase_kf = """ psql -h 10.91.23.186 "dbname=kaifa_%s user=gpadmin password=gpadmin"  -t  -c \"  """ % (dbip)

    # 源端表是否存在-> 不存在给出提示
    if exitTab(sqlBase_ori, dbname, tabname) == 1:

        #  判断目标端表是否存在  0不存在: 分别在开发测试建表 todo 修改为0
        print("=======create tar table ===========")
        if exitTab(sqlBase_kf, dbname, tabname) == 0:
            print(" --------------- create tar faifa table ---------------")
            outsql = "pg_dump csgbi -s --gp-syntax -x -h %s -U gpadmin -p 5432 -t  %s -f %s.sql" % (oriIP, db_table, db_table)
            sub.run(outsql, shell=True)
            print(outsql)

            insql = "psql -h 10.91.23.186 \"dbname=kaifa_%s user=gpadmin password=gpadmin\" -f %s.sql" % (dbip, db_table)
            sub.run(insql, shell=True)
            print(insql)

            # sub.run("rm -f %s.sql" % (db_table), shell=True)

            # 为用户授权
            grantUse(sqlBase_kf, dbname, tabname, username)

        if exitTab(sqlBase_cs, dbname, tabname) == 0:
            print(" --------------- create tar ceshi table ---------------")
            outsql = "pg_dump csgbi -s --gp-syntax -x -h %s -U gpadmin -p 5432 -t  %s -f %s.sql" % (oriIP, db_table, db_table)
            sub.run(outsql, shell=True)
            print(outsql)

            insql = "psql -h 10.91.23.186 \"dbname=ceshi_%s user=gpadmin password=gpadmin\" -f %s.sql" % (dbip, db_table)
            sub.run(insql, shell=True)
            sub.run("rm -f %s.sql" % (db_table), shell=True)
            # 为用户授权
            grantUse(sqlBase_cs, dbname, tabname, username)


        # 数据量为0 导入数据
        print("=======data transmission  ===========")
        if couTab(sqlBase_kf, dbname, tabname) == 0:
            print(" ---------------   ceshi   ---------------")

            #  导出数据文件:       psql -h 10.92.208.37 -p 5432 -U gpadmin -d csgbi -c "\copy (select * from DWZC.TWB_M_SP_PD_FAULT_REPORT_1_PRT_P03  where   1=1   limit 10000 ) to '/data1/aa.dat' with csv header "
            outCsv = " psql -h %s -p 5432 -U gpadmin -d csgbi -c \"\copy (select * from %s  %s   limit 10000 ) to '/data1/%s.dat' with csv header \" " % (oriIP, db_table, where, db_table)
            print(outCsv)
            sub.run(outCsv, shell=True)

            #  导入数据文件       psql -h 10.91.23.186 "dbname=kaifa_37 user=gpadmin password=gpadmin" -c "\copy DWZC.TWB_M_SP_PD_FAULT_REPORT from '/data1/aa.dat' with csv header "
            inCsvKf = " psql -h 10.91.23.186 \"dbname=kaifa_%s user=gpadmin password=gpadmin\" -c \"\copy %s from '/data1/%s.dat' with csv header \" " % (dbip, db_table, db_table)
            sub.run(inCsvKf, shell=True)
            print(inCsvKf)

            # 删除数据文件
            sub.run("rm -f /data1/%s.dat" % (db_table), shell=True)

        if couTab(sqlBase_cs, dbname, tabname) == 0:
            print(" --------------- kaifa ---------------")

            #  导出数据文件:       psql -h 10.92.208.37 -p 5432 -U gpadmin -d csgbi -c "\copy (select * from DWZC.TWB_M_SP_PD_FAULT_REPORT_1_PRT_P03  where   1=1   limit 10000 ) to '/data1/aa.dat' with csv header "
            outCsv = " psql -h %s -p 5432 -U gpadmin -d csgbi -c \"\copy (select * from %s  %s   limit 10000 ) to '/data1/%s.dat' with csv header \" " % (oriIP, db_table, where, db_table)
            print(outCsv)
            sub.run(outCsv, shell=True)

            #  导入数据文件       psql -h 10.91.23.186 "dbname=kaifa_37 user=gpadmin password=gpadmin" -c "\copy DWZC.TWB_M_SP_PD_FAULT_REPORT from '/data1/aa.dat' with csv header "
            inCsvCs = " psql -h 10.91.23.186 \"dbname=ceshi_%s user=gpadmin password=gpadmin\" -c \"\copy %s from '/data1/%s.dat' with csv header \" " % (dbip, db_table, db_table)
            sub.run(inCsvCs, shell=True)
            print(inCsvCs)

            # 删除数据文件
            sub.run("rm -f /data1/%s.dat" % (db_table), shell=True)


    # 不存在 给提示
    else:
        print("error: ori table no exit , please check out ")
