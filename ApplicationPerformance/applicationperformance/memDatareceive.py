import os
import time
import applicationperformance.cpuDatareceive as cpuDatareceive #Mac系统 导入模块重命名
import applicationperformance.launchTime as launchTime
class MemoryApplicationData(object):

    #获取内存的数据
    def receiveMemoryCmd(self,searchkey,devicesid):
        if "Windows" in cpuDatareceive.CpuApplicationData().receiveSystomInfo() :
            pass
        elif "Darwin" in cpuDatareceive.CpuApplicationData().receiveSystomInfo():
            if devicesid != "":  # 有devicesid
                executememorycmd = os.popen("adb -s %s shell dumpsys meminfo | grep %s" % (devicesid, searchkey))
                memoryinfo = []
                memorycounts = 0
                for x in executememorycmd:
                    memoryinfo.append(x.strip())
                memoryinfo = memoryinfo[0:3]
                for memorycount in memoryinfo:
                    memorycounts = memorycounts + (int(memorycount.split('kB')[0].strip()))
                return str(memorycounts / 1024) + 'MB'
            else:
                executememorycmd = os.popen("adb shell dumpsys meminfo | grep %s" % (searchkey))
                memoryinfo = []
                memorycounts = 0
                for x in executememorycmd:
                    memoryinfo.append(x.strip())
                memoryinfo = memoryinfo[0:3]
                for memorycount in memoryinfo:
                    memorycounts = memorycounts + (int(memorycount.split('kB')[0].strip()))
                return str(memorycounts / 1024) + 'MB'
        else:
            print("当前系统环境无法识别，请使用Mac或Windows系统")

    def receiveMemoryData(self):
        caserows = launchTime.ReadExcel().readeExcelData('memorydata')
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
                        cpuDatareceive.CpuApplicationData().monkeyRun(monkeyscript)  # 运行monkey脚本
                        memorydatas = ""  # 统计执行monkey时，获取的CPU值。
                        while count > 0:
                            startruntime = time.time()
                            memorydata = MemoryApplicationData().receiveMemoryCmd(searchkey, devicesid)
                            memorydatas = memorydatas + memorydata + ","
                            endruntime = time.time()
                            runtime = int(str(endruntime - startruntime).split(".")[1][0:4])
                            runtimes = endruntime - startruntime
                            time.sleep(intervaltime)
                            count -= 1
                            print("用例编号：%s,第%s次执行，执行时间为：%s ms,执行结果为：%s" % (caseid, runnumber, runtime, memorydata))
                            runnumber += 1
                        if memorydatas.endswith(','):  # 处理cpuproportions字符串，把结尾的逗号去掉
                            memorydatas = memorydatas.rstrip(',')
                        savedata = "insert into automation_mem_app  (`memorysize`,`starttime`,`endtime`,`monkeyscript`,`functionscript`,`createdtime`,`updatetime`,`caseid`,`runtime`,`eventid`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            memorydatas, startruntime, endruntime, monkeyscript, functionscript,
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, runtimes, eventid)
                        launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                        cpuDatareceive.CpuApplicationData().monkeyRun(monkeyscript)  # 停止monkey脚本
                    elif functionscript != "":
                        # 执行自动化测试用例的脚本
                        startruntime = time.time()
                        while count > 0:
                            receivecpudata = cpuDatareceive.CpuApplicationData().receiveCpuDataCmd(searchkey, devicesid)
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
                            memorydata = MemoryApplicationData().receiveMemoryCmd(searchkey, devicesid)
                            endruntime = time.time()
                            runtime = int(str(endruntime - startruntime).split(".")[1][0:4])
                            runtimes = endruntime - startruntime
                            savedata = "insert into automation_mem_app  (`memorysize`,`starttime`,`endtime`,`monkeyscript`,`functionscript`,`createdtime`,`updatetime`,`caseid`,`runtime`,`eventid`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                                memorydata, startruntime, endruntime, monkeyscript, functionscript,
                                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), caseid, runtimes, eventid)
                            launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                            print("用例编号：%s,第%s次执行，执行时间为：%s ms,执行结果为：%s" % (caseid, runnumber, runtime, memorydata))
                            time.sleep(intervaltime)
                            count -= 1
                            runnumber += 1
                else:
                    print("用例编号:%s，该用例执行次数为0，则不执行，用例数据为：%s" % (caseid, returndata))
            elif 'N' in executestatus:
                print("用例编号:%s，该用例执行状态为NO，则不执行，用例数据为：%s" % (caseid, returndata))
            else:
                print("用例编号:%s，该用例未执行，请检查该用例状态是否为Yes或No.用例数据为：%s" % (caseid, returndata))


#if __name__ == "__main__":
    #print(MemoryApplicationData().receiveMemoryCmd('zhuishushenqi','emulator-5554'))

if __name__ == "__main__":
    MemoryApplicationData().receiveMemoryData()