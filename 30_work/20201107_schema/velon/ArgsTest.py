import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='dictlauncher...')
    parser.add_argument("--company-code", type=str)
    parser.add_argument("--domain", type=str)
    parser.add_argument("--dbtype", type=str)
    args = parser.parse_args()

    print(args)

    part = ""
    if args.company_code:
        part += " and s.company_code = '" + args.company_code + "'"
    if args.domain:
        part += " and s.domain = '" + args.domain + "'"
    if args.dbtype:
        part += " and s.dbtype = '" + args.dbtype + "'"

    querySql = """
            SELECT
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
               WHERE d.`pk_type`=1 """ + part + \
               """
              ORDER BY
               s.company_code,
               s.domain,
               s.table_name
               """
    print(querySql)
