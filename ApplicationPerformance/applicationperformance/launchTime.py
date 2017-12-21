import time
import pymysql
import os
import xlrd


class LaunchApplication(object):
    # 冷启动APP
    def coolLaunch(self, packactivity, devicesid):
        if devicesid != "":
            launchcmd = 'adb -s %s shell am start -W -n %s' % (devicesid, packactivity)
            launchtcmddata = os.popen(launchcmd)
            return launchtcmddata
        else:
            launchcmd = 'adb shell am start -W -n %s' % (packactivity)
            launchtcmddata = os.popen(launchcmd)
            return launchtcmddata

    # 停止APP
    def stopApp(self, packname, devicesid):
        if devicesid != "":
            stopcmd = 'adb -s %s shell am force-stop %s' % (devicesid, packname)
            stopcmddata = os.popen(stopcmd)
            return stopcmddata
        else:
            stopcmd = 'adb shell am force-stop %s' % (packname)
            stopcmddata = os.popen(stopcmd)
            return stopcmddata

    # 热启动
    def hotLaunch(self,devicesid):
        if devicesid != "":
            hotLaunchcmd = 'adb -s %s shell input keyevent 3'%(devicesid)
            hotLaunchcmddata = os.popen(hotLaunchcmd)
        else:
            hotLaunchcmd = 'adb shell input keyevent 3'
            hotLaunchcmddata = os.popen(hotLaunchcmd)
    #获取设备ID 暂时不用
    def receiveDevices(self):
        devicesid = os.popen("adb devices")
        devices = []
        for x in devicesid:
            if 'attached' not in x:
                x = x.strip('\r\n')
                devices.append(x)
        return devices

    # 运行且保存数据
    def runApp(self):
        startcasetime = time.time()
        try:
            caserows = ReadExcel().readeExcelData('launchtime')
            eventid = time.strftime("%Y%m%d%H%M%S", time.localtime())
            for i in range(1, caserows.get('caserows')):
                casedata = caserows.get('excledata_sheel').row_values(i)
                caseid = int(casedata[0])
                packactivity = casedata[1]
                packname = casedata[2]
                launchtype = casedata[3]
                count = int(casedata[4])
                devicesid = casedata[5]
                returndata = caseid, packactivity, packname, launchtype, count, devicesid
                if count > 0:
                    print("执行用例编号:%s，用例数据为：%s" % (caseid, returndata))
                    if launchtype == 'C':
                        launchcount = 1  # 记录启动次数
                        while count > 0:
                            starttime = time.time()
                            launchtcmddata = LaunchApplication().coolLaunch(packactivity, devicesid)  # 热启动APP
                            for launchtimes in launchtcmddata:
                                if "ThisTime" in launchtimes:
                                    launchtime = launchtimes.split(':')[1].strip() + 'ms'
                                    endtime = time.time()
                                    print("第%s次启动时间为：" % (launchcount), launchtime)
                                    time.sleep(5)
                                    LaunchApplication().stopApp(packname, devicesid)  # 关闭APP
                                    savedata = "insert into automation_Launch_app  (`starttime`,`launchtime`,`endtime`,`launchtype`,`createdtime`,`updatetime`,`caseid`,`eventid`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                        starttime, launchtime, endtime, launchtype,
                                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid,eventid)
                                    MysqlConnect().saveDatatoMysql("%s" % (savedata))
                                    time.sleep(2)
                                    break
                            count -= 1
                            launchcount += 1
                    elif launchtype == 'H':  # 热启动方法，冷启动-back-热启动
                        launchcount = 1  # 记录启动次数
                        while count > 0:
                            LaunchApplication().coolLaunch(packactivity, devicesid)  # 冷启动APP
                            time.sleep(5)
                            starttime = time.time()
                            LaunchApplication().hotLaunch(devicesid)  # back
                            launchtcmddata = LaunchApplication().coolLaunch(packactivity, devicesid)  # 热启动APP
                            for launchtimes in launchtcmddata:
                                if "ThisTime" in launchtimes:
                                    launchtime = launchtimes.split(':')[1].strip() + 'ms'
                                    endtime = time.time()
                                    print(launchtime)
                                    time.sleep(5)
                                    LaunchApplication().stopApp(packname, devicesid)  # 关闭APP
                                    savedata = "insert into automation_Launch_app  (`starttime`,`launchtime`,`endtime`,`launchtype`,`createdtime`,`updatetime`,`caseid`,`eventid`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                        starttime, launchtime, endtime, launchtype,
                                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, eventid)
                                    MysqlConnect().saveDatatoMysql("%s" % (savedata))
                                    time.sleep(2)
                                    break
                            count -= 1
                            launchcount += 1
                    else:
                        print("您的启动类型有错，请检查您的启动类型")
                else:
                    print("用例编号:%s，该用例不执行，用例数据为：%s" % (caseid, returndata))
        except:
            print("请检查您的用例，查看是否有错")
        endtimecasetime = time.time()
        print("执行用例时间为:%ss" % (round(endtimecasetime - startcasetime, 2)))


# 数据库连接和保存测试结果
class MysqlConnect(object):
    def queryDatatoMysql(self, sql):  # 查询数据
        connect = pymysql.connect(
            host='steel.iask.in',
            port=33067,
            user='huangshunyao',
            password='Hsy5332#',
            db='automation_db',
            charset='utf8',  # 解决中文乱码
        )
        # connect = pymysql.connect(
        #     host='192.168.1.9',  # 测试环境
        #     port=33006,
        #     user='huangshunyao',
        #     passwd='Hsy5332#',  # 注意password
        #     db='automation_db',
        #     charset='utf8',  # 解决中文乱码
        # )

        cursor = connect.cursor()  # 获取游标
        cursor.execute(sql)  # 执行sql语句
        data = cursor.fetchone()  # 获取数据
        connect.close()  # 关闭链接
        return data

    def saveDatatoMysql(self, sql):  # 保存数据
        # connect = pymysql.connect(
        #     host='192.168.1.9',  # 测试环境
        #     port=33006,
        #     user='huangshunyao',
        #     passwd='Hsy5332#',  # 注意password
        #     db='automation_db',
        #     charset='utf8',  # 解决中文乱码
        # )
        connect = pymysql.connect(
            host='steel.iask.in',
            port=33067,
            user='huangshunyao',
            password='Hsy5332#',
            db='automation_db',
            charset='utf8',  # 解决中文乱码
        )
        cursor = connect.cursor()  # 获取游标
        cursor.execute(sql)  # 执行sql语句
        connect.commit()  # 提交数据
        connect.close()  # 关闭链接


# 读取用例
class ReadExcel(object):
    def readeExcelData(self, launchtime):
        if launchtime == 'launchtime':
            excelcase = xlrd.open_workbook("Testcase.xlsx")
            excledata_sheel = excelcase.sheet_by_name('launchtime')
            caserows = excledata_sheel.nrows
            returndata = {'caserows': caserows, 'excledata_sheel': excledata_sheel}
            return returndata
        elif launchtime == 'cpudata':
            excelcase = xlrd.open_workbook("one.xlsx")
            excledata_sheel = excelcase.sheet_by_name('cpudata')
            caserows = excledata_sheel.nrows
            returndata = {'caserows': caserows, 'excledata_sheel': excledata_sheel}
            return returndata
        elif launchtime == 'memorydata':
            excelcase = xlrd.open_workbook("one.xlsx")
            excledata_sheel = excelcase.sheet_by_name('memorydata')
            caserows = excledata_sheel.nrows
            returndata = {'caserows': caserows, 'excledata_sheel': excledata_sheel}
            return returndata
        else:
            return "Excel中无该工作目录"

if __name__ == "__main__":
    LaunchApplication().runApp()
