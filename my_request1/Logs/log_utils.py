import sys
import os
import datetime
base_path = os.getcwd()    # 获取当前路径
sys.path.append(base_path)  # 将当前路径添加到系统路径中


import logging
from Config import Conf
import datetime
from Config.Conf import Reader_config
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR,
}
class Logs:
    
    def __init__(self,log_file,log_name,log_level):
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(log_l[self.log_level])
        if not self.logger.handlers:
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
            fh_stream.setFormatter(formatter)

            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)

            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


log_path = Conf.get_logs()
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
log_extension = Reader_config().get_conf_log_extension()
file_name = os.path.join(log_path,current_time+log_extension)

loglevel = Reader_config().get_conf_log_level()

def my_log(log_name = __file__):
    return Logs(log_file=file_name,log_name=log_name,log_level=loglevel).logger

if __name__ == '__main__':
    my_log().debug("dsadasd")   # debug("dsadasd") 是日子级别 和描述，用于日志模版
