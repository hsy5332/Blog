import applicationperformance.launchTime as launchTime  # Mac系统
# import ApplicationPerformance.applicationperformance.launchTime as launchTime #windows 系统 引入applicationperformance.launchTime 模块重命名为launchTime
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
                cpudatas = []
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                for i in receivecpudata:
                    cpudatas.append(i)
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'
            else:
                receivecpucmd = "adb.exe shell dumpsys cpuinfo | find %s" % (searchkey)
                cpudatas = []
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                for i in receivecpudata:
                    cpudatas.append(i)
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'
        elif "Linux" in CpuApplicationData().receiveSystomInfo():  # Linux系统
            if devicesid != "":
                receivecpucmd = "adb -s %s shell dumpsys cpuinfo | grep %s" % (devicesid, searchkey)
                cpudatas = []
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                for i in receivecpudata:
                    cpudatas.append(i)
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'
            else:
                receivecpucmd = "adb shell dumpsys cpuinfo | grep %s" % (searchkey)
                cpudatas = []
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                for i in receivecpudata:
                    cpudatas.append(i)
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'
        elif "Darwin" in CpuApplicationData().receiveSystomInfo():  # Mac系统
            if devicesid != "":
                receivecpucmd = "adb -s %s shell dumpsys cpuinfo | grep %s" % (devicesid, searchkey)
                cpudatas = []
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                for i in receivecpudata:
                    cpudatas.append(i)
                print(cpudatas)
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'

            else:
                receivecpucmd = "adb shell dumpsys cpuinfo | grep %s" % (searchkey)
                cpudatas = []
                cpuproportion = 0
                receivecpudata = os.popen(receivecpucmd)
                for i in receivecpudata:
                    cpudatas.append(i)
                for cpuproportiondatas in cpudatas:
                    cpuproportiondata = float(cpuproportiondatas.split('%')[0])
                    cpuproportion = cpuproportion + cpuproportiondata
                return str(cpuproportion) + '%'
        else:
            print("当前系统环境有问题，无法识别当前系统属性。")

    # 执行monkey脚本
    def monkeyRun(self, monkeyscript):
        monkeycmd = os.popen(monkeyscript)

    # 停止运行monkey
    def Stopmonkey(self, devicesid):
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
        for i in range(1, caserows.get('caserows')):
            casedata = caserows.get('excledata_sheel').row_values(i)
            caseid = int(casedata[0])
            packactivity = casedata[1]
            packname = casedata[2]
            searchkey = casedata[3]
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
                        cpuproportions = ""  # 统计执行monkey时，获取的CPU值。
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
                        savedata = "insert into automation_cpu_app  (`cpuproportion`,`starttime`,`endtime`,`monkeyscript`,`functionscript`,`createdtime`,`updatetime`,`caseid`,`runtime`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            cpuproportions, startruntime, endruntime, monkeyscript, functionscript,
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, runtimes)
                        launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                        CpuApplicationData().Stopmonkey(devicesid)  # 停止monkey脚本
                    elif functionscript != "":
                        # 执行自动化测试用例的脚本
                        startruntime = time.time()
                        while count > 0:
                            receivecpudata = CpuApplicationData().receiveCpuDataCmd(searchkey, devicesid)
                            for cpudatas in receivecpudata:
                                cpudatas = cpudatas.split("%")
                                cpudata = cpudatas[0].strip() + "%"
                                print(cpudata)
                            time.sleep(intervaltime)
                            count -= 1
                        print("我是functionstatus")
                        endruntime = time.time()
                    else:
                        launchTime.LaunchApplication().coolLaunch(packactivity, devicesid)
                        runnumber = 1
                        while count > 0:
                            startruntime = time.time()
                            cpuproportion = CpuApplicationData().receiveCpuDataCmd(searchkey, devicesid)
                            endruntime = time.time()
                            runtime = int(str(endruntime - startruntime).split(".")[1][0:4])
                            runtimes = endruntime - startruntime
                            savedata = "insert into automation_cpu_app  (`cpuproportion`,`starttime`,`endtime`,`monkeyscript`,`functionscript`,`createdtime`,`updatetime`,`caseid`,`runtime`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                cpuproportion, startruntime, endruntime, monkeyscript, functionscript,
                                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, runtimes)
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
