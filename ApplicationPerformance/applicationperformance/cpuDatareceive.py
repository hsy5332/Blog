import applicationperformance.launchTime as launchTime  # Mac系统
#import ApplicationPerformance.applicationperformance.launchTime as launchTime #windows 系统 引入applicationperformance.launchTime 模块重命名为launchTime
import applicationfunction.functionAutomation as functionAutomation
import os
import time
import platform


class CpuApplicationData(object):

    # 判断当前系统
    def receiveSystomInfo(self):
        return platform.system()

    # 执行CPU百分比命令
    def receiveCpuDataCmd(self, searchkey, devicesid):
        if "Windows" in CpuApplicationData().receiveSystomInfo():  # Windows系统
            if devicesid != "":
                receivecpucmd = "adb.exe -s %s shell dumpsys cpuinfo | find \"%s\"" % (devicesid, searchkey)
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                cpudatas = [i for i in receivecpudata]
                while "\n" in cpudatas:
                    cpudatas.remove("\n")
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'
            else:
                receivecpucmd = "adb.exe shell dumpsys cpuinfo | find \"%s\"" % (searchkey)
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                cpudatas = [i for i in receivecpudata]
                while "\n" in cpudatas:
                    cpudatas.remove("\n")
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'
        elif "Darwin" in CpuApplicationData().receiveSystomInfo():  # Mac系统
            if devicesid != "":
                receivecpucmd = "adb -s %s shell dumpsys cpuinfo | grep %s" % (devicesid, searchkey)
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                cpudatas = [i for i in receivecpudata]
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'

            else:
                receivecpucmd = "adb shell dumpsys cpuinfo | grep %s" % (searchkey)
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                cpudatas = [i for i in receivecpudata]
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'
        else:
            print("当前系统环境无法识别，请使用Mac或Windows系统")

    # 执行monkey脚本
    def monkeyRun(self, monkeyscript):
        monkeycmd = os.popen(monkeyscript)

    # 停止运行monkey
    def Stopmonkey(self, devicesid):
        if "Windows" in CpuApplicationData().receiveSystomInfo():  # Windows系统
            if devicesid != "":
                executecmd = [i for i in os.popen("adb -s %s shell ps | find \"monkey\"" % (devicesid))]
                while "\n" in executecmd:
                    executecmd.remove("\n")
                stopmonkeycmd = executecmd[0].split()[1]
                os.popen("adb -s %s shell kill -9 %s" % (devicesid, stopmonkeycmd))
            else:
                executecmd = [i for i in os.popen("adb shell ps | find \"monkey\"")]
                while "\n" in executecmd:
                    executecmd.remove("\n")
                stopmonkeycmd = executecmd[0].split()[1]
                os.popen("adb shell kill -9 %s" % (stopmonkeycmd))
        elif "Darwin" in CpuApplicationData().receiveSystomInfo():  # Mac系统
            if devicesid != "":
                for i in os.popen("adb -s %s shell ps | grep monkey" % (devicesid)):
                    stopmonkeycmd = i.split()[1]
                    os.popen("adb -s %s shell kill -9 %s" % (devicesid, stopmonkeycmd))
            else:
                for i in os.popen("adb shell ps | grep monkey"):
                    stopmonkeycmd = i.split()[1]
                    os.popen("adb shell kill -9 %s" % (stopmonkeycmd))
        else:
            if devicesid != "":
                for i in os.popen("adb -s %s shell ps | grep monkey" % (devicesid)):
                    stopmonkeycmd = i.split()[1]
                    os.popen("adb -s %s shell kill -9 %s" % (devicesid, stopmonkeycmd))
            else:
                for i in os.popen("adb shell ps | grep monkey"):
                    stopmonkeycmd = i.split()[1]
                    os.popen("adb shell kill -9 %s" % (stopmonkeycmd))

    # 获取CPU数据且保存数据
    def receiveCpuData(self):
        caserows = launchTime.ReadExcel().readeExcelData('cpudata')
        eventid = time.strftime('%Y%m%d%H%M%S', time.localtime())
        for i in range(1, caserows.get('caserows')):
            casedata = caserows.get('excledata_sheel').row_values(i)
            caseid = int(casedata[0])
            packactivity = casedata[1]
            packname = casedata[2]
            searchkey = casedata[3]
            if searchkey == "":
                print("执行命令的搜索字为空，请检查excel表格D1列")
            monkeyscript = casedata[4]
            functionscript = casedata[5]
            count = int(casedata[6])
            intervaltime = int(casedata[7])
            devicesid = casedata[8]
            executestatus = casedata[9]
            returndata = caseid, packname, monkeyscript, functionscript, count, intervaltime, devicesid, executestatus
            if 'Y' in executestatus:
                if count > 0:
                    print("执行用例编号:%s，用例数据为：%s" % (caseid, returndata))
                    if monkeyscript != "":
                        runnumber = 1
                        CpuApplicationData().monkeyRun(monkeyscript)  # 运行monkey脚本
                        cpuproportions = ""  # 统计执行monkey时，获取CPU值。
                        while count > 0:
                            startruntime = time.time()
                            cpuproportion = CpuApplicationData().receiveCpuDataCmd(searchkey, devicesid)
                            cpuproportions = cpuproportions + cpuproportion + ","
                            endruntime = time.time()
                            runtime = int(str(endruntime - startruntime).split(".")[1][0:4])
                            runtimes = endruntime - startruntime
                            time.sleep(intervaltime)
                            count -= 1
                            print("用例编号：%s,第%s次执行，执行时间为：%s ms,执行结果为：%s" % (caseid, runnumber, runtime, cpuproportion))
                            runnumber += 1
                        if cpuproportions.endswith(','):  # 处理cpuproportions字符串，把结尾的逗号去掉
                            cpuproportions = cpuproportions.rstrip(',')
                        savedata = "insert into automation_cpu_app  (`cpuproportion`,`starttime`,`endtime`,`monkeyscript`,`functionscript`,`createdtime`,`updatetime`,`caseid`,`runtime`,`eventid`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            cpuproportions, startruntime, endruntime, monkeyscript, functionscript,
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, runtimes, eventid)
                        launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                        CpuApplicationData().Stopmonkey(devicesid)  # 停止monkey脚本
                    elif functionscript != "":
                        functionAutomation.FunctionAutomation().runTestCase("open")  # 执行自动化测试用例
                        runnumber = 1
                        while count > 0:
                            startruntime = time.time()
                            cpuproportion = CpuApplicationData().receiveCpuDataCmd(searchkey, devicesid)
                            endruntime = time.time()
                            runtime = int(str(endruntime - startruntime).split(".")[1][0:4])
                            runtimes = endruntime - startruntime
                            savedata = "insert into automation_cpu_app  (`cpuproportion`,`starttime`,`endtime`,`monkeyscript`,`functionscript`,`createdtime`,`updatetime`,`caseid`,`runtime`,`eventid`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                cpuproportion, startruntime, endruntime, monkeyscript, functionscript,
                                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, runtimes, eventid)
                            launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                            print("用例编号：%s,第%s次执行，执行时间为：%s ms,执行结果为：%s" % (caseid, runnumber, runtime, cpuproportion))
                            time.sleep(intervaltime)
                            count -= 1
                            runnumber += 1
                    else:
                        launchTime.LaunchApplication().coolLaunch(packactivity, devicesid)
                        runnumber = 1
                        while count > 0:
                            startruntime = time.time()
                            cpuproportion = CpuApplicationData().receiveCpuDataCmd(searchkey, devicesid)
                            endruntime = time.time()
                            runtime = int(str(endruntime - startruntime).split(".")[1][0:4])
                            runtimes = endruntime - startruntime
                            savedata = "insert into automation_cpu_app  (`cpuproportion`,`starttime`,`endtime`,`monkeyscript`,`functionscript`,`createdtime`,`updatetime`,`caseid`,`runtime`,`eventid`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                cpuproportion, startruntime, endruntime, monkeyscript, functionscript,
                                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, runtimes, eventid)
                            launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                            print("用例编号：%s,第%s次执行，执行时间为：%s ms,执行结果为：%s" % (caseid, runnumber, runtime, cpuproportion))
                            time.sleep(intervaltime)
                            count -= 1
                            runnumber += 1
                else:
                    print("用例编号:%s，该用例执行次数为0，则不执行，用例数据为：%s" % (caseid, returndata))
            elif 'N' in executestatus:
                print("用例编号:%s，该用例执行状态为NO，则不执行，用例数据为：%s" % (caseid, returndata))
            else:
                print("用例编号:%s，该用例未执行，请检查该用例状态是否为Yes或No.用例数据为：%s" % (caseid, returndata))


if __name__ == "__main__":
    CpuApplicationData().receiveCpuData()
