import sys
import os
base_path = os.getcwd()    # 获取当前路径
sys.path.append(base_path) 
from Read_yaml.yaml_utils import Reader_Yaml
current = os.path.abspath(__file__) # 当前路径
base_dir = os.path.dirname(os.path.dirname(current)) #获取当前项目上上一级路径俩个  嵌套方法
config_path = base_dir+os.sep + "config"

config_yaml_path = config_path+os.sep + "conf_yaml.yaml"

log_payh = base_dir + os.sep + 'Logs'

db_config_file = config_path + os.sep + 'db_conf.yaml'

def get_config():
    return config_path

def get_yaml():
    return config_yaml_path

def get_logs():
    return log_payh

def get_db():
    return db_config_file

class Reader_config:

    def __init__(self):
        self.config = Reader_Yaml(get_yaml()).data()
        self.db_config = Reader_Yaml(get_db()).data()

    def get_excel_file(self):
        return self.config["BASE"]["test"]["case_file"]

    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]

    def get_conf_log_level(self):
        return self.config["BASE"]["log_level"]

    def get_conf_db(self,db_alisa):
        return self.db_config[db_alisa]

        
