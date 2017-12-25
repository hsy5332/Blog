import applicationperformance.launchTime as launchTime
from appium import webdriver
import time
class FunctionAutomation(object):

    #初始化设备，读取设备信息
    def originalDevices(self,deviceName,platformName,platformVersion,appPackage,appActivity):
        devicesinfo = {}
        devicesinfo['deviceName'] = deviceName
        devicesinfo['platformName'] = platformName
        devicesinfo['platformVersion'] = platformVersion
        devicesinfo['appPackage'] = appPackage
        devicesinfo['appActivity'] = appActivity
        return devicesinfo

    #连接设备
    def connectDevices(self):
        pass

    #断开设备连接
    def stopConnectDevices(self):
        pass

    #点击事件
    def operateClick(self):
        pass

    #滑动操作
    def operateslide(self,direction):
        pass

    #长按操作
    def operateLongClick(self):
        pass

    #运行用例
    def runTestCase(self):
        deviceinfo = launchTime.ReadExcel().readeExcelData('deviceinfo')
        for i in range(1, deviceinfo.get('caserows')):
            casedata = deviceinfo.get('excledata_sheel').row_values(i)
            print(casedata)
            deviceName = casedata[0]
            platformName= casedata[1]
            platformVersion = casedata[2]
            appPackage = casedata[3]
            appActivity = casedata[4]
            port = int(casedata[5])
            devicesinfo =FunctionAutomation().originalDevices(deviceName,platformName,platformVersion,appPackage,appActivity)
            driver = webdriver.Remote('http://localhost:%s/wd/hub' % (port), devicesinfo)
            time.sleep(10)
            driver.quit()


FunctionAutomation().runTestCase()