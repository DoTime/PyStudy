from dict.OracleMetaHandler import OracleMetaHandler
from dict.MysqlMetaHandler import MysqlMetaHandler
from dict.DmMetaHandler import DmMetaHandler
from util import MysqlUtil
from util.IdWorker import IdWorker

if __name__ == '__main__':

    worker = IdWorker(1, 1)
    # 查询mysql的系统信息，获得需要查询表结构的所有表名

    # where db_type = 'mysql' and s.company_code = 99

    result = MysqlUtil.query(
        """ SELECT
                s.table_id,
                s.company_code,
                s.domain,
                s.table_schema,
                s.table_name,
                s.db_type,
                d.`table_name` AS table_name_des
           FROM
            src_table_extra_info s
            JOIN info_des_table_view d ON s.`table_id` = d.`table_id`
           WHERE s.db_type = 'mysql' AND d.`pk_type`=1
           ORDER BY
            s.company_code,
            s.domain,
            s.table_name """
    )

    # result = range(0, 1)

    if (result):
        for item in result:
            # item = list()

            # item.append('11111')
            # item.append('99')
            # item.append('local')
            # item.append('csg_info')
            # item.append('src_table_extra_info')
            # item.append('mysql')
            # item.append('des')

            # table_id
            # company_code
            # domain
            # table_schema
            # table_name
            # db_type
            # table_name_des

            print("===item===")
            print(item)

            table_id = item[0]
            company_code = item[1]
            domain = item[2]
            table_schema = item[3]
            table_name = item[4]
            db_type = item[5]
            table_name_des = None

            creTableSql = """
                    CREATE TABLE IF NOT EXISTS `src_table_dict_%s_%s`  (
                      `column_id` bigint(20) NOT NULL,
                      `domain` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '域',
                      `company_code` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '分省',
                      `sys_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '系统名称',
                      `table_schema` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '表所有者,模式名,数据库名',
                      `table_name` varchar(155) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '表名',
                      `table_name_zh` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '表名中文名称',
                      `column_position` decimal(3, 0) NULL DEFAULT NULL COMMENT '列序号',
                      `column_name` varchar(155) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '列名',
                      `pk` varchar(2) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '是否为主健，Y表示是，N表示否',
                      `data_type` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '数据类型',
                      `data_length` decimal(20, 0) NULL DEFAULT NULL COMMENT '数据长度',
                      `data_precision` decimal(4, 0) NULL DEFAULT NULL COMMENT '数字长度',
                      `data_scale` decimal(4, 0) NULL DEFAULT NULL COMMENT '数字小数精度',
                      `data_default` text CHARACTER SET utf8 COLLATE utf8_general_ci NULL COMMENT '默认值',
                      `nullable` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '是否为空 Y表示是，N表示否',
                      `table_comment` varchar(6144) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '表注释',
                      `column_comment` varchar(6144) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '字段注释',
                      `remark` varchar(6144) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT '备注',
                      `date_time` datetime(0) NULL DEFAULT NULL,
                      `table_name_des` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL COMMENT 'kudu表名',
                      PRIMARY KEY (`column_id`) USING BTREE 
                ) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci  ROW_FORMAT = Compact;        
                """ % (company_code, domain)

            MysqlUtil.upsert(creTableSql)

            # 删除旧数据
            delSql = "delete from src_table_dict_%s_%s " \
                     "  where company_code='%s' and domain='%s' and table_schema='%s' and table_name='%s'" % (
                         company_code, domain, company_code, domain, table_schema, table_name)

            MysqlUtil.upsert(delSql)

            # 回调逻辑
            obj = eval(db_type[0].upper() + db_type[1:] + "MetaHandler()")
            dicts = obj.handle(item)

            insertSqlBatch = """
                  insert into csg_info.src_table_dict_""" + company_code + "_" + domain + \
                             """(      column_id        
                                      ,domain
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
                                      ,date_time
                                      ,table_name_des 
                                       )                
                                 values  ( 
                                           %s,%s,%s,%s,%s 
                                          ,%s,%s,%s,%s,%s 
                                          ,%s,%s,%s,%s,%s 
                                          ,%s,%s,%s,%s,%s
                                          ,%s
                                          )  """

            MysqlUtil.upsert_batch(insertSqlBatch, dicts)
