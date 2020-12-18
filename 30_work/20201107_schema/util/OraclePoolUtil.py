from DBUtils.PooledDB import PooledDB
from conf import config, log
import cx_Oracle
import threading

pools = {}
lock = threading.RLock()


def pool(dsn, user, password, idle=5):
    with lock:
        global pools
        if (not dsn in pools):
            p = PooledDB(cx_Oracle,
                         mincached=idle,
                         maxcached=idle,
                         user=user,
                         password=password,
                         dsn=dsn
                         # dsn="%s:%s/%s" % (config.oracle_host, config.oracle_port, config.oracle_db)
                         )
            pools[dsn] = p
    pass
    return pools[dsn]


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
        log.logger.error("Error: Function happen Error: query")
    finally:
        cur.close()
        conn.close()


if __name__ == '__main__':
    p = pool("%s:%s/%s" % (config.oracle_host, config.oracle_port, config.oracle_db), config.oracle_user,
             config.oracle_password)
    query(p, 'SELECT * from AAA')
