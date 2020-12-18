# -- coding: utf-8 --
# # Filename mysqlInsertMany.py
# import mysql.connector
#
# from dict.AbstractMetaHandler import SrcTableDict
#
# host = "10.92.172.50",
# port = 20015,
# user = "deltalake",
# passwd = "Deltalake..172",
# database = "csg_info",
# charset = "utf8"
#
# a, b = 2, 1
# c = (a > b and [a] or [b])[0]
# print(c)
#
#
#
# print('True' if 2 > 1 else 'False')
#
# print("===")
# conls = SrcTableDict()
# conls.set_domain("Nonesdfsd")
# domain = conls.get_domain()
# print(domain)

#
# if __name__ == '__main__':
#     list=[]
#     list.append("ddd")
#     print(len(list))
import pymysql
from DBUtils.PooledDB import PooledDB

from conf import config
from dict import MysqlMetaHandler
from dict.AbstractMetaHandler import SrcTableDict


def aggSetGet():
    list = {
        'column_id',
        'domain',
        'company_code',
        'sys_name',
        'table_schema',
        'table_name',
        'table_name_zh',
        'column_position',
        'column_name',
        'data_type',
        'data_length',
        'data_precision',
        'data_scale',
        'data_default',
        'pk',
        'nullable',
        'table_comment',
        'column_comment',
        'remark',
        'date_time',
        'table_name_des'
    }
    print(list)

    for col in list:
        str = """
            def get_""" + col + """(self):
                return self.__""" + col + """
            def set_""" + col + """(self, val):
                if val is not None: self.__""" + col + """ = val
            """

        print(str)


def t1():
    val = None
    if (val):
        print("111")


# t1()

def inMysqlNull():
    pool = PooledDB(pymysql, mincached=3, maxcached=300, host=config.mysql_host, user=config.mysql_user,
                    passwd=config.mysql_password, db=config.mysql_db, port=config.mysql_port,
                    charset=config.mysql_charset)  # 5为连接池里的最少连接数

    # 调用连接池
    conn = pool.connection()
    a = None
    par = a
    parList = list()
    # parList.append(par)
    # parList.append("111")
    # parList.append("1331")
    # parList.append(par)
    #
    parList.append (('ff','22'))
    parList.append (('Adfam','122'))
    parList.append (('Adafm','2332'))
    parList.append (('ff',None))

    # sql = " insert into csg_info.t1  values  ('aa')  "

    # sql = "INSERT INTO   VALUES (%s) "
    abc = "null"
    sql = "insert into    csg_info.t1  values (%s,%s)"

    cur = conn.cursor()
    print(parList)
    cur.executemany(sql, parList)

    # abc = None
    # l = []
    # l.append(abc)
    # cur.execute(sql, l)

    conn.commit()


# inMysqlNull()

def getPojoAttr():
    item = list()

    item.append('11111')
    item.append('99')
    item.append('local')
    item.append('csg_info')
    item.append('src_table_extra_info')
    item.append('mysql')
    item.append('des')

    handle = MysqlMetaHandler.handle(item)



