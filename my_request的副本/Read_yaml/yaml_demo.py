import sys
import os
base_path = os.getcwd()    # 获取当前路径
sys.path.append(base_path)  # 将当前路径添加到系统路径中
import yaml

""" with open("/Users/chenshuai/Desktop/my_request/yaml/one_yaml.yaml","r",encoding="utf-8") as f:
    f = yaml.safe_load(f)
    print(f)  """

""" with open("/Users/chenshuai/Desktop/my_request/yaml/two_yaml.yaml","r",encoding="utf-8") as f:
    f = yaml.safe_load_all(f)
    a = []ß
    for i in f:
        a.append(i)
    print(a) """
