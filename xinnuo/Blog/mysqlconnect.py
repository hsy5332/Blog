import MySQLdb

def sqlconnect(sql):

    db = MySQLdb.connect(
        host = '192.168.26.62',
        port = 3306,
        user = 'root',
        password = '123',
        db = 'test',
)
    cursor = db.cursor() #获取游标
    cursor.execute(sql) #执行sql语句
    data = cursor.fetchone() #获取数据
    db.close() #关闭sql连接
    return data

# 此方法慎用!!
