import pymysql
from conf import config, log
from DBUtils.PooledDB import PooledDB
import threading

pools = {}
lock = threading.RLock()


def pool(url, user, password, port, db, idle=5):
    with lock:
        global pools
        if not (url + user + password) in pools:
            p = PooledDB(pymysql, idle,
                         host=url, user=user, passwd=password, db=db, port=port,
                         charset=config.mysql_charset)  # 5为连接池里的最少连接数
            pools[url + user + password] = p
    pass
    return pools[url + user + password]


def upsert(pool, sql):
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


def upsert_batch(pool, sql, list):
    """
        demo:
        SQL 批量插入语句
        sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME); VALUES (%s,%s,%s,%s,%s)"
        区别与单条插入数据，VALUES ('%s', '%s',  %s,  '%s', %s) 里面不用引号
        list = [('li', 'si', 16, 'F', 1000), ('Bruse', 'Jerry', 30, 'F', 3000), ('Lee', 'Tomcat', 40, 'M', 4000), ('zhang', 'san', 18, 'M', 1500)]
    :param sql:
    :param list:
    :return:
    """
    log.logger.debug(sql)
    try:
        # 调用连接池
        conn = pool.connection()
        cur = conn.cursor()
        cur.executemany(sql, list)
    except IOError:
        conn.rollback()  # 出现异常 回滚事件
        log.logger.error("Error: Function happen Error: upsert_batch")
    finally:
        cur.close()
        conn.close()
    pass


def query(pool, sql):
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


if __name__ == "__main__":
    # p= pool("%s:%s/%s" % (config.oracle_host, config.oracle_port, config.oracle_db),config.oracle_user,config.oracle_password)
    # query(p,"SELECT src.`table_id`, src.`company_code`, src.`domain`, src.`table_schema`, src.`table_name`, des.`rows` FROM  src_table_info src JOIN des_table_extra_info des ON src.`table_id`=des.`table_id` where src.company_code='04' and src.domain ='cw' and src.table_schema='fmis0200' and src.table_name='rc_intervalgrade_syssetting'")
    pass
