from conf import log, config
import subprocess


def shell(sql):
    """
    调用impala查询记录数
    :param company_code:
    :param domain:
    :param table_name:
    :return:
    """

    impala_cmd = "impala-shell -i {impala_host}:{impala_port} -B -q '{sql}'" \
        .format(impala_host=config.impala_host,
                impala_port=config.impala_port,
                sql=sql)
    log.logger.info(impala_cmd)
    statusoutput = subprocess.getstatusoutput(impala_cmd)
    return statusoutput


def shell_(sql):
    """
    调用impala查询记录数
    :param company_code:
    :param domain:
    :param table_name:
    :return:
    """

    impala_cmd = "impala-shell -i {impala_host}:{impala_port} -B -q {sql}" \
        .format(impala_host=config.impala_host,
                impala_port=config.impala_port,
                sql=sql)
    log.logger.info(impala_cmd)
    statusoutput = subprocess.getstatusoutput(impala_cmd)
    return statusoutput

# def query(sql):
#     log.logger.debug(sql)
#
#     try:
#         # 调用连接池
#         conn = impala.connect(host=config.impala_host, port=config.impala_port)
#         cur = conn.cursor()
#         cur.execute(sql)
#         result = cur.fetchall()
#         return result
#     except IOError:
#         log.logger.error("Error: Function happen Error: query")
#     finally:
#         cur.close()
#         conn.close()
