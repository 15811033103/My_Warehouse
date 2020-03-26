import sys
import os
base_path = os.getcwd()    # 获取当前路径
sys.path.append(base_path) 
from Logs.log_utils import my_log
import json

class Assert:
    def __init__(self):
        self.log = my_log("Assert_utils")

    def assert_code(self,code,expected_code):

        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code error ,code is %s ,expected is %s"%(code,expected_code))
            raise 
    
    def assert_body(self,body,expected_body):
        """
        验证body 和预期结果是否一致
        :param body:
        :param expected_body:
        :return:
        """
        try:
            assert body == expected_body
            return True
        except:
            self.log.error("body== error ,body is %s,expected_body is %s"%(body,expected_body))   
            raise 

    def assert_body_in(self,body,expected_body):
        """
        验证预期结果是否在body中
        :param body:
        :param expected_body:
        :return:
        """
        try:
            body = json.dumps(body)
            assert expected_body in body
            return True
        except:
            self.log.error("预期结果 不在body 中 error ,body is %s,expected_body is %s"%(body,expected_body))   
            raise 