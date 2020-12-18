import pymysql
from conf import config,log
from DBUtils.PooledDB import PooledDB

pool = PooledDB(pymysql, mincached=3,maxcached=300, host=config.mysql_host, user=config.mysql_user, passwd=config.mysql_password, db=config.mysql_db, port=config.mysql_port, charset=config.mysql_charset) #5为连接池里的最少连接数

def upsert(sql):
    log.logger.debug(sql)
    try:
        # 调用连接池
        conn = pool.connection()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except IOError:
        conn.rollback()  # 出现异常 回滚事件
        log.logger.error("Error: Function happen Error: upsert")
    finally:
        cur.close()
        conn.close()
    pass


def upsert_batch(sql,list):
    """
        demo:
        SQL 批量插入语句
        sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME); VALUES (%s,%s,%s,%s,%s)"
        区别与单条插入数据，VALUES ('%s', '%s',  %s,  '%s', %s) 里面不用引号
        list = (('li', 'si', 16, 'F', 1000), ('Bruse', 'Jerry', 30, 'F', 3000), ('Lee', 'Tomcat', 40, 'M', 4000), ('zhang', 'san', 18, 'M', 1500))
    :param sql:
    :param list:
    :return:
    """
    log.logger.debug(sql)
    try:
        # 调用连接池
        conn = pool.connection()
        cur = conn.cursor()
        cur.executemany(sql,list)
        conn.commit()
    except IOError:
        conn.rollback()  # 出现异常 回滚事件
        log.logger.error("Error: Function happen Error: upsert_batch")
    finally:
        cur.close()
        conn.close()
    pass


def query(sql):
    log.logger.debug(sql)

    try:
        # 调用连接池
        conn = pool.connection()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        return result
    except IOError:
        log.logger.error("Error: Function happen Error: execute_query")
    finally:
        cur.close()
        conn.close()


if __name__=="__main__":
    query("SELECT src.`table_id`, src.`company_code`, src.`domain`, src.`table_schema`, src.`table_name`, des.`rows` FROM  src_table_info src JOIN des_table_extra_info des ON src.`table_id`=des.`table_id` where src.company_code='04' and src.domain ='cw' and src.table_schema='fmis0200' and src.table_name='rc_intervalgrade_syssetting'")