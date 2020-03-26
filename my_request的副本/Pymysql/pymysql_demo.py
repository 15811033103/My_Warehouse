import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'chenshua1',
    database = 'test_db'
)
cursor = conn.cursor()
sql = "select username ,password from cs_db"
cursor.execute(sql)
res = cursor.fetchone()
print(res)
cursor.close()
conn.close()