import applicationperformance.launchTime
import os
import time


class CpuApplicationData(object):
    def receiveCpuDataCmd(self, packname, devicesid):
        if devicesid != "":
            receivecpucmd = "adb -s %s shell dumpsys cpuinfo | grep %s" % (devicesid, packname)
            receivecpudata = os.popen(receivecpucmd)
            return receivecpudata
        else:
            receivecpucmd = "adb shell dumpsys cpuinfo | grep %s" % (packname)
            receivecpudata = os.popen(receivecpucmd)
            return receivecpudata

    # 执行monkey脚本
    def monkeyRun(self, monkeyscript):
        monkeycmd = os.popen(monkeyscript)


    # 获取CPU数据且保存数据
    def receiveCpuData(self):
        caserows = applicationperformance.launchTime.ReadExcel().readeExcelData('cpudata')
        for i in range(1, caserows.get('caserows')):
            casedata = caserows.get('excledata_sheel').row_values(i)
            caseid = int(casedata[0])
            packname = casedata[1]
            monkeyscript = casedata[2]
            functionscript = casedata[3]
            count = int(casedata[4])
            intervaltime = int(casedata[5])
            devicesid = casedata[6]
            returndata = caseid, packname, monkeyscript, functionscript, count, intervaltime, devicesid
            if count > 0:
                print("执行用例编号:%s，用例数据为：%s" % (caseid, returndata))
                if monkeyscript != "":
                    startruntime = time.time()
                    counts = 1
                    while count > 0:
                        CpuApplicationData().monkeyRun(monkeyscript)
                        startruntime = time.time()
                        receivecpudata = CpuApplicationData().receiveCpuDataCmd(packname, devicesid)
                        for cpudatas in receivecpudata:
                            cpudatas = cpudatas.split("%")
                            cpuproportion = cpudatas[0].strip() + "%"
                        endruntime = time.time()
                        runtime = int(str(endruntime - startruntime).split(".")[1][0:4])
                        runtimes = endruntime - startruntime
                        savedata = "insert into automation_cpu_app  (`cpuproportion`,`starttime`,`endtime`,`monkeyscript`,`functionscript`,`createdtime`,`updatetime`,`caseid`,`runtime`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            cpuproportion, startruntime, endruntime, monkeyscript, functionscript,
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, runtimes)
                        applicationperformance.launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                        print("用例编号：%s,第%s次执行，执行时间为：%s ms。" % (caseid, counts, runtime))
                        time.sleep(intervaltime)
                        count -= 1
                        counts += 1
                elif functionscript != "":
                    # 执行自动化测试用例的脚本
                    startruntime = time.time()
                    while count > 0:
                        receivecpudata = CpuApplicationData().receiveCpuDataCmd(packname, devicesid)
                        for cpudatas in receivecpudata:
                            cpudatas = cpudatas.split("%")
                            cpudata = cpudatas[0].strip() + "%"
                            print(cpudata)
                        time.sleep(intervaltime)
                        count -= 1
                    print("我是functionstatus")
                    endruntime = time.time()
                else:
                    counts  = 1
                    while count > 0:
                        startruntime = time.time()
                        receivecpudata = CpuApplicationData().receiveCpuDataCmd(packname, devicesid)
                        for cpudatas in receivecpudata:
                            cpudatas = cpudatas.split("%")
                            cpuproportion = cpudatas[0].strip() + "%"
                        endruntime = time.time()
                        runtime = int(str(endruntime - startruntime).split(".")[1][0:4])
                        runtimes = endruntime - startruntime
                        savedata = "insert into automation_cpu_app  (`cpuproportion`,`starttime`,`endtime`,`monkeyscript`,`functionscript`,`createdtime`,`updatetime`,`caseid`,`runtime`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            cpuproportion, startruntime, endruntime, monkeyscript, functionscript,
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, runtimes)
                        applicationperformance.launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                        print("用例编号：%s,第%s次执行，执行时间为：%s ms。" % (caseid,counts, runtime))
                        time.sleep(intervaltime)
                        count -= 1
                        counts += 1
            else:
                print("用例编号:%s，该用例不执行，用例数据为：%s" % (caseid, returndata))


if __name__ == "__main__":
    CpuApplicationData().receiveCpuData()
