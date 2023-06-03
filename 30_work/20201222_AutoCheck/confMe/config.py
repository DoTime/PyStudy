import configparser
import os

cfg = configparser.ConfigParser()
cfg.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini"), encoding="utf-8")

# 获取配置文件信息

mysql_host = cfg['mysql']['host']
mysql_port = int(cfg['mysql']['port'])
mysql_user = cfg['mysql']['user']
mysql_password = cfg['mysql']['password']
mysql_db = cfg['mysql']['db']
mysql_charset = cfg['mysql']['charset']

oracle_host = cfg['oracle']['host']
oracle_port = int(cfg['oracle']['port'])
oracle_user = cfg['oracle']['user']
oracle_password = cfg['oracle']['password']
oracle_db = cfg['oracle']['db']
oracle_charset = cfg['oracle']['charset']
