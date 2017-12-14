import pymysql


class MysqlConnect(object):
    def saveDatatoMysql(self, sql):
        connect = pymysql.connect(
            host='steel.iask.in',
            port=33067,
            user='huangshunyao',
            password='Hsy5332#',
            db='automation_db',
        )
        cursor = connect.cursor()  # 获取游标
        cursor.execute(sql)  # 执行sql语句
        data = cursor.fetchone()  # 获取数据
        connect.close()  # 关闭链接
        return data

# print(MysqlConnect().saveDatatoMysql('select * from automation_launch_app'))
