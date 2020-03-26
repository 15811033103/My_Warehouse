import sys
import os
base_path = os.getcwd()   
sys.path.append(base_path)
from Config.Conf import Reader_config
from Pymysql.pymysql_utils import My_db

def init_db(db_alisa):
    db_info = Reader_config().get_conf_db(db_alisa)
    host = db_info['db_host']
    user = db_info["db_user"]
    password = db_info["db_password"]
    database = db_info["db_name"]
    conn = My_db(host,user,password,database)
    print(conn)
    return conn

#a = init_db("db_1")
