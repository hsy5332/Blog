import ApplicationPerformance.applicationperformance.launchTime


class CpuApplicationData(object):
    #执行monkey脚本
    def monkeyRun(self):
        pass

    #获取CPU数据且保存数据
    def receiveCpuData(self):
        caserows = ApplicationPerformance.applicationperformance.launchTime.ReadExcel().readeExcelData('cpudata')
        
CpuApplicationData().receiveCpuData()