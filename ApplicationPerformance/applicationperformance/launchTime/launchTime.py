import time
import pymysql
import os


class LaunchApplication(object):
    # 冷启动APP
    def coolLaunch(self, packactivity):
        # packactivity = "com.ushaqi.zhuishushenqi/com.ushaqi.zhuishushenqi.ui.SplashActivity"
        launchcmd = 'adb shell am start -W -n %s' % (packactivity)
        launchtcmddata = os.popen(launchcmd)
        return launchtcmddata

    # 停止APP
    def stopApp(self, packname):
        stopcmd = 'adb shell am force-stop %s' % (packname)
        stopcmddata = os.popen(stopcmd)
        return stopcmddata

    # 热启动
    def hotLaunch(self):
        hotLaunchcmd = 'adb shell input keyevent 3'
        hotLaunchcmddata = os.popen(hotLaunchcmd)

    # 运行且保存数据
    def runApp(self, launchtype, count, packactivity, packname, caseid):
        if launchtype == 'C':
            launchcount = 1  # 记录启动次数
            while count > 0:
                starttime = time.time()
                launchtcmddata = LaunchApplication().coolLaunch(packactivity)  # 热启动APP
                for launchtimes in launchtcmddata:
                    if "ThisTime" in launchtimes:
                        launchtime = launchtimes.split(':')[1].strip() + 'ms'
                        endtime = time.time()
                        print("第%s次启动时间为：" % (launchcount), launchtime)
                        time.sleep(5)
                        LaunchApplication().stopApp(packname)  # 关闭APP
                        savedata = "insert into automation_Launch_app  (`starttime`,`launchtime`,`endtime`,`launchtype`,`createdtime`,`updatetime`,`caseid`)VALUES('%s','%s','%s','%s','%s','%s','%s')" % (
                            starttime, launchtime, endtime, launchtype,
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid)
                        time.sleep(2)
                        break
                count -= 1
                launchcount += 1
        elif launchtype == 'H':  # 热启动方法，冷启动-back-热启动
            launchcount = 1  # 记录启动次数
            while count > 0:
                LaunchApplication().coolLaunch(packactivity)  # 热启动APP
                time.sleep(5)
                starttime = time.time()
                LaunchApplication().hotLaunch()  # back
                launchtcmddata = LaunchApplication().coolLaunch(packactivity)  # 热启动APP
                for launchtimes in launchtcmddata:
                    if "ThisTime" in launchtimes:
                        launchtime = launchtimes.split(':')[1].strip() + 'ms'
                        endtime = time.time()
                        print(launchtime)
                        time.sleep(5)
                        LaunchApplication().stopApp(packname)  # 关闭APP
                        savedata = "insert into automation_Launch_app  (`starttime`,`launchtime`,`endtime`,`launchtype`,`createdtime`,`updatetime`,`caseid`)VALUES('%s','%s','%s','%s','%s','%s','%s')" % (
                            starttime, launchtime, endtime, launchtype,
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid)
                        MysqlConnect().saveDatatoMysql("%s" % (savedata))
                        time.sleep(2)
                        break
                count -= 1
                launchcount += 1
        else:
            print("您的启动类型有错，请检查您的启动类型")


class MysqlConnect(object):
    def queryDatatoMysql(self, sql):  # 查询数据库数据
        # connect = pymysql.connect(
        #     host='steel.iask.in',
        #     port=33067,
        #     user='huangshunyao',
        #     password='Hsy5332#',
        #     db='automation_db',
        #     charset = 'utf8', #解决中文乱码
        # )
        connect = pymysql.connect(
            host='192.168.1.9',  # 测试环境
            port=33006,
            user='huangshunyao',
            passwd='Hsy5332#',  # 注意password
            db='automation_db',
            charset='utf8',  # 解决中文乱码
        )

        cursor = connect.cursor()  # 获取游标
        cursor.execute(sql)  # 执行sql语句
        data = cursor.fetchone()  # 获取数据
        connect.close()  # 关闭链接
        return data

    def saveDatatoMysql(self, sql):  # 保存数据
        connect = pymysql.connect(
            host='192.168.1.9',  # 测试环境
            port=33006,
            user='huangshunyao',
            passwd='Hsy5332#',  # 注意password
            db='automation_db',
            charset='utf8',  # 解决中文乱码
        )

        cursor = connect.cursor()  # 获取游标
        cursor.execute(sql)  # 执行sql语句
        connect.commit()  # 提交数据
        connect.close()  # 关闭链接


LaunchApplication().runApp('C', 2, "com.ushaqi.zhuishushenqi/com.ushaqi.zhuishushenqi.ui.SplashActivity",
                           "com.ushaqi.zhuishushenqi", 1)
