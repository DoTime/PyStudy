import configparser
import os
import yaml

cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.dirname(os.path.abspath(__file__)),"config_linux.ini"), encoding="utf-8")

app=yaml.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'app.yml'),'r'), Loader=yaml.FullLoader)


#获取配置文件信息
cdh_version=cfg['cdh']['version']

flinkx_cmd_path=cfg['flinkx']['cmd_path']
flinkx_log_dir=cfg['flinkx']['log_dir']

impala_host=cfg['impala']['host']
impala_port=cfg['impala']['port']


yarn_url = cfg['yarn']['url']

hdfs_http_url= cfg['hdfs']['http_url']
hdfs_user_name=cfg['hdfs']['user_name']

mysql_host = cfg['mysql']['host']
mysql_port = int(cfg['mysql']['port'])
mysql_user = cfg['mysql']['user']
mysql_password = cfg['mysql']['password']
mysql_db = cfg['mysql']['db']
mysql_charset = cfg['mysql']['charset']



# oracle_host = cfg['oracle']['host']
# oracle_port = int(cfg['oracle']['port'])
# oracle_user = cfg['oracle']['user']
# oracle_password = cfg['oracle']['password']
# oracle_db = cfg['oracle']['db']
# oracle_charset = cfg['oracle']['charset']





