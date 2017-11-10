import MySQLdb

db = MySQLdb.connect(
    host = 'loaclhost',
    port = 3306,
    user = 'root',
    password = '123',
    db = 'test',
)
cursor = db.cursor() #获取游标
sql = "" #编写sql语句

cursor.execute(sql) #执行sql语句
data = cursor.fetchone() #获取数据
db.close() #关闭sql连接

