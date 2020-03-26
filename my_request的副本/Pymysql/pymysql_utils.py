import sys
import os
base_path = os.getcwd()    
sys.path.append(base_path)  
from Logs.log_utils import my_log
import pymysql
class My_db:

    def __init__(self,host,user,password,database):
        self.log = my_log()
        self.conn = pymysql.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def fetchone(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("sql执行通过，执行的语句是%s"%(sql))
            return True
        except Exception as e:
            print("sql执行错误")

    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()
        print("连接已关闭")

if __name__ == '__main__':
    mysql = My_db("localhost","root","chenshua1","test_db")
    mysql.exec("update cs_db set password='SUSUsu1' where username='chenshuai'")