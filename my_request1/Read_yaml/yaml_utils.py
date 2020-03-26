import sys
import os
base_path = os.getcwd()    # 获取当前路径
sys.path.append(base_path) 
import os
import yaml

class Reader_Yaml:

    def __init__(self,yaml):
        if os.path.exists(yaml):
            self.yaml = yaml
        else:
            raise FileNotFoundError("文件不存在")
        self._data=None
        self._data_all=None

    def data(self):
        if not self._data:
            with open(self.yaml,"r",encoding="utf-8") as f:
                self._data = yaml.safe_load(f)
        return self._data

    def data_all(self):
        if not self._data_all:
            with open(self.yaml,"r",encoding="utf-8") as f:
                self._data = yaml.safe_load_all(f)
        return self._data_all