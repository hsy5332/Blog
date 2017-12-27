import applicationperformance.launchTime as launchTime
from appium import webdriver
import time


class FunctionAutomation(object):
    # 初始化设备，读取设备信息
    def originalDevices(self, deviceName, platformName, platformVersion, appPackage, appActivity, udid):
        devicesinfo = {}
        devicesinfo['deviceName'] = deviceName
        devicesinfo['platformName'] = platformName
        devicesinfo['platformVersion'] = platformVersion
        devicesinfo['appPackage'] = appPackage
        devicesinfo['appActivity'] = appActivity
        devicesinfo['udid'] = udid
        return devicesinfo

    # 连接设备
    def connectDevices(self):
        pass

    # 断开设备连接
    def stopConnectDevices(self):
        pass

    # 点击事件
    def operateClick(self, operatetype, element, driver, caseid):

        if operatetype == "点击_id":
            try:
                driver.find_element_by_id(element).click()  # 点击ID事件
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "点击_xpath":
            try:
                driver.find_element_by_xpath(element).click()  # 点击xpath
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))

    # 滑动操作
    def operateslide(self, direction):
        pass

    # 长按操作
    def operateLongClick(self):
        pass

    # 运行用例
    def runTestCase(self):
        deviceinfo = launchTime.ReadExcel().readeExcelData('deviceinfo')
        for i in range(1, deviceinfo.get('caserows')):
            devicescase = deviceinfo.get('excledata_sheel').row_values(i)
            deviceName = devicescase[0]  # 设备名称
            udid = devicescase[0]  # 设备uid
            platformName = devicescase[1]  # 系统名称
            platformVersion = devicescase[2]  # 系统版本
            appPackage = devicescase[3]  # 测试APP的包名
            appActivity = devicescase[4]  # 测试AppActivity
            port = int(devicescase[5])  # 连接Appium端口号
            devicesinfo = FunctionAutomation().originalDevices(deviceName, platformName, platformVersion,
                                                               appPackage, appActivity, udid)  # 连接测试设备
            casedata = launchTime.ReadExcel().readeExcelData('funcase')  # 读取自动化用例数据
            if platformName == "Android":
                try:
                    driver = webdriver.Remote('http://localhost:%s/wd/hub' % (port), devicesinfo)  # 连接Appium
                    time.sleep(3)
                    startcasetime = time.time()  # 开始执行用例时间
                    for x in range(1, casedata.get('caserows')):  # Excel中的测试用例数据，使用for遍历每一行的数据，进行判断执行对应的操作
                        excelcasedata = casedata.get('excledata_sheel').row_values(
                            x)
                        caseid = int(excelcasedata[0])  # 用例编号
                        operatetype = excelcasedata[1]  # 操作类型
                        element = excelcasedata[2]  # 元素属性
                        parameter = excelcasedata[3]  # 参数（如：输入的数据）
                        checkpoint = excelcasedata[4]  # 检查点对比
                        if excelcasedata[5] == "":
                            waittime = 2
                        else:
                            waittime = int(excelcasedata[5])  # 等待时间
                        if "Y" in excelcasedata[7]:
                            if operatetype == "点击_id":  # 根据ID点击
                                FunctionAutomation().operateClick(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "点击_xpath":  # 根据xpath点击
                                FunctionAutomation().operateClick(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "test":
                                pass
                            else:
                                print("用例编号:%s操作类型错误,该用例不执行。" % (caseid))
                        else:
                            print("用例编号:%s,执行状态为No,故不执行。" % (caseid))
                    driver.quit()  # 关闭Appium的连接
                    endtimecasetime = time.time()  # 结束用例执行时间
                    print("执行用例时间为:%ss" % (round(endtimecasetime - startcasetime, 2)))  # 计算执行用例运行时间
                except:
                    driver.quit()
                    print("请检查Appium和设备是否正常连接。")
            elif platformName == "IOS":
                pass
            else:
                print("当前系统名称输入错误，请输入正确的设备系统，Android或IOS。")


FunctionAutomation().runTestCase()
