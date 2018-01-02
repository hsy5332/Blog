import applicationperformance.launchTime as launchTime  # MAC
# import ApplicationPerformance.applicationperformance.launchTime as launchTime  # Windows
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException  # 导入selenium NoSuchElementException异常模块


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
        devicesinfo['unicodeKeyboard'] = "True"
        devicesinfo['resetKeyboard'] = "True"
        return devicesinfo

    # 断开APP连接
    def stopConnectAppium(self):
        pass

    # 点击事件
    def operateClick(self, operatetype, element, driver, caseid, *parameter):

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
        elif operatetype == "点击_textname":  # 点击textname
            try:
                driver.find_elements_by_name(element)[0].click()
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))

        elif operatetype == "点击_classid":
            try:
                driver.find_elements_by_class_name(element)[0].click()  # 点击xpath
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        else:
            print("用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid))

    # 滑动操作
    def operateslide(self, operatetype, driver, caseid):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        if operatetype == "向上滑动":
            try:
                driver.swipe(x * 0.5, y * 0.9, x * 0.5, y * 0.3)
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "向左滑动":
            try:
                driver.swipe(x * 0.9, y * 0.5, x * 0.08, y * 0.5)
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "向下滑动":
            try:
                driver.swipe(x * 0.5, y * 0.3, x * 0.5, y * 0.9)
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "向右滑动":
            try:
                driver.swipe(x * 0.08, y * 0.5, x * 0.9, y * 0.5)
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        else:
            print("用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid))

    # 检查元素是否存在
    def operateCheckelement(self, operatetype, element, driver, caseid):
        if operatetype == "查找_id":
            try:
                driver.find_element_by_id(element)
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "查找_xpath":
            try:
                driver.find_element_by_xpath(element)
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "查找_classid":
            try:
                driver.find_elements_by_class_name(element)
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "查找_textname":
            try:
                driver.find_elements_by_name(element)[0]  # 注意 此方法在appium高版本上 可能无法运行
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "if包含_id":
            try:
                driver.find_element_by_id(element)
                return ("用例编号:%s,执行通过。" % (caseid))
            except:
                return ("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "if包含_xpath":
            try:
                driver.find_element_by_xpath(element)
                return ("用例编号:%s,执行通过。" % (caseid))
            except:
                return ("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "if包含_classid":
            try:
                driver.find_elements_by_class_name(element)
                return ("用例编号:%s,执行通过。" % (caseid))
            except:
                return ("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "if包含_textname":
            try:
                driver.find_elements_by_name(element)[0]
                return ("用例编号:%s,执行通过。" % (caseid))
            except:
                return ("用例编号:%s,执行不通过。" % (caseid))
        else:
            return ("用例编号:%s,执行不通过，该用例的元素属性可能有问题，请检查该用例。" % (caseid))

    # 拖拽操作
    def operateDrag(self):
        pass

    # 长按操作
    def operateLongClick(self, operatetype, element, driver, caseid, *parameter):
        if operatetype == "长按_id":  # 长按元素id
            try:
                el = driver.find_element_by_id(element)
                TouchAction(driver).long_press(el, 1).release().perform()
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "长按_classid":  # 长按元素classname
            try:
                el = driver.find_elements_by_class_name(element)[0]
                TouchAction(driver).long_press(el, 1).release().perform()
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "长按_xpath":  # 长按元素xpath
            try:
                el = driver.find_element_by_xpath(element)
                TouchAction(driver).long_press(el, 1).release().perform()
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "长按_textname":  # 长按textname
            try:
                el = driver.find_elements_by_name(element)[0]
                TouchAction(driver).long_press(el, 1).release().perform()
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        else:
            print("用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid))

    # 输入操作
    def operateInput(self, operatetype, element, driver, caseid, *parameter):
        if operatetype == "输入_id":
            try:
                driver.find_element_by_id(element).send_keys(parameter[0])
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "输入_xpath":
            try:
                driver.find_element_by_xpath(element).send_keys(parameter[0])
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "输入_classid":
            try:
                driver.find_elements_by_class_name(element)[0].send_keys(parameter[0])
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "输入_textname":
            try:
                driver.find_elements_by_name(element)[0].send_keys(parameter[0])
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        else:
            print("用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid))

    # Android物理按键操作
    def operatePhysicsKye(self, driver, caseid, *parameter):
        keycode = parameter[0]
        try:
            driver.keyevent(keycode)
            print("用例编号:%s,执行通过。" % (caseid))
        except:
            print("用例编号:%s,执行不通过。" % (caseid))

    # 运行用例
    def runTestCase(self, isquit):
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
            devicesexecute = devicescase[7]  # 执行状态
            devicesinfos = "设备名：" + str(deviceName) + "," + "系统版本信息：" + str(platformName) + str(platformVersion)
            eventid = time.strftime('%Y%m%d%H%M%S', time.localtime())
            if "Y" in devicesexecute:
                devicesinfo = FunctionAutomation().originalDevices(deviceName, platformName, platformVersion,
                                                                   appPackage, appActivity, udid)  # 连接测试设备
                casedata = launchTime.ReadExcel().readeExcelData('funcase')  # 读取自动化用例数据
                endcasenumber = []
                casenumber = []
                for j in range(1, casedata.get('caserows')):  # Excel中的测试用例数据，使用for遍历每一行的数据，进行判断执行对应的操作
                    excelcasedata = casedata.get('excledata_sheel').row_values(
                        j)
                    operatetype = excelcasedata[1]
                    if "if" in operatetype:
                        casenumber.append(j)
                    if "end" in operatetype:
                        endcasenumber.append(j)
                if platformName == "Android":
                    # try:
                    driver = webdriver.Remote('http://localhost:%s/wd/hub' % (port), devicesinfo)  # 连接Appium
                    startcasetime = time.time()  # 开始执行用例时间
                    x = 1
                    ifnumber = 0
                    startonecasetime = time.time()
                    while x < casedata.get('caserows'):  # Excel中的测试用例数据，使用for遍历每一行的数据，进行判断执行对应的操作
                        excelcasedata = casedata.get('excledata_sheel').row_values(
                            x)
                        x = x + 1
                        caseid = int(excelcasedata[0])  # 用例编号
                        operatetype = excelcasedata[1]  # 操作类型
                        element = excelcasedata[2]  # 元素属性
                        parameter = excelcasedata[3]  # 参数（如：输入的数据）x
                        checkpoint = excelcasedata[4]  # 检查点对比
                        rundescribe = excelcasedata[6]
                        caseexecute = excelcasedata[7]
                        if excelcasedata[5] == "":
                            waittime = 2
                        else:
                            waittime = int(excelcasedata[5])  # 等待时间
                        if "Y" in caseexecute:
                            if operatetype == "等待时间":
                                time.sleep(waittime)
                                print("用例编号:%s,执行通过。" % (caseid))
                            elif operatetype == "点击_id":  # 根据ID点击
                                FunctionAutomation().operateClick(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "点击_xpath":  # 根据xpath点击
                                FunctionAutomation().operateClick(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "点击_classid":
                                FunctionAutomation().operateClick(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "点击_textname":
                                FunctionAutomation().operateClick(operatetype, element, driver, caseid)
                            elif operatetype == "向上滑动":
                                FunctionAutomation().operateslide(operatetype, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "向左滑动":
                                FunctionAutomation().operateslide(operatetype, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "向下滑动":
                                FunctionAutomation().operateslide(operatetype, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "向右滑动":
                                FunctionAutomation().operateslide(operatetype, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "长按_id":
                                FunctionAutomation().operateLongClick(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "长按_xpath":
                                FunctionAutomation().operateLongClick(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "长按_classid":
                                FunctionAutomation().operateLongClick(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "长按_textname":
                                FunctionAutomation().operateLongClick(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "输入_id":
                                FunctionAutomation().operateInput(operatetype, element, driver, caseid, parameter)
                                time.sleep(waittime)
                            elif operatetype == "输入_xpath":
                                FunctionAutomation().operateInput(operatetype, element, driver, caseid, parameter)
                                time.sleep(waittime)
                            elif operatetype == "输入_classid":
                                FunctionAutomation().operateInput(operatetype, element, driver, caseid, parameter)
                                time.sleep(waittime)
                            elif operatetype == "输入_textname":
                                FunctionAutomation().operateInput(operatetype, element, driver, caseid, parameter)
                                time.sleep(waittime)
                            elif operatetype == "物理按钮":
                                FunctionAutomation().operatePhysicsKye(driver, caseid, int(parameter))
                                time.sleep(waittime)
                            elif operatetype == "点击_确认":
                                FunctionAutomation().operatePhysicsKye(driver, caseid, 66)
                                time.sleep(waittime)
                            elif operatetype == "点击_返回":
                                FunctionAutomation().operatePhysicsKye(driver, caseid, 4)
                                time.sleep(waittime)
                            elif operatetype == "查找_id":
                                FunctionAutomation().operateCheckelement(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "查找_xpath":
                                FunctionAutomation().operateCheckelement(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "查找_classid":
                                FunctionAutomation().operateCheckelement(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif operatetype == "查找_textname":
                                FunctionAutomation().operateCheckelement(operatetype, element, driver, caseid)
                                time.sleep(waittime)
                            elif "if" in operatetype:
                                if operatetype == "if包含_id":
                                    executeresult = FunctionAutomation().operateCheckelement(operatetype, element,
                                                                                             driver, caseid)
                                    if "执行通过" in executeresult:
                                        print(executeresult)
                                    else:
                                        print(executeresult)
                                        # try:
                                        #     x = endcasenumber[ifnumber]
                                        # except IndexError:
                                        #     if len(endcasenumber) - 1 >= 0:
                                        #         x = endcasenumber[len(endcasenumber) - 1]
                                        #         print("当前用例中的if和and不等，请检查用例")
                                        #     else:
                                        #         print("当前用例中的if和and不等，请检查用例")
                                        #         pass
                                        if len(endcasenumber) == len(casenumber):
                                            x = endcasenumber[ifnumber]
                                        else:
                                            print("当前用例中的if和and不等，请检查用例")
                                            x = endcasenumber[-1]
                                elif "if包含_xpath":
                                    executeresult = FunctionAutomation().operateCheckelement(operatetype, element,
                                                                                             driver, caseid)
                                    if "执行通过" in executeresult:
                                        print(executeresult)
                                    else:
                                        print(executeresult)
                                        if len(endcasenumber) == len(casenumber):
                                            x = endcasenumber[ifnumber]
                                        else:
                                            print("当前用例中的if和and不等，请检查用例")
                                            x = endcasenumber[-1]
                                elif "if包含_classid":
                                    executeresult = FunctionAutomation().operateCheckelement(operatetype, element,
                                                                                             driver, caseid)
                                    if "执行通过" in executeresult:
                                        print(executeresult)
                                    else:
                                        print(executeresult)
                                        if len(endcasenumber) == len(casenumber):
                                            x = endcasenumber[ifnumber]
                                        else:
                                            print("当前用例中的if和and不等，请检查用例")
                                            x = endcasenumber[-1]
                                elif "if包含_textname":
                                    executeresult = FunctionAutomation().operateCheckelement(operatetype, element,
                                                                                             driver, caseid)
                                    if "执行通过" in executeresult:
                                        print(executeresult)
                                    else:
                                        print(executeresult)
                                        if len(endcasenumber) == len(casenumber):
                                            x = endcasenumber[ifnumber]
                                        else:
                                            print("当前用例中的if和and不等，请检查用例")
                                            x = endcasenumber[-1]
                                else:
                                    print("用例编号:%s操作类型错误,该用例不执行。" % (caseid))
                                ifnumber = ifnumber + 1
                            elif operatetype == "end":
                                print("用例编号:%s,执行通过。" % (caseid))
                            else:
                                print("用例编号:%s操作类型错误,该用例不执行。" % (caseid))
                        else:
                            print("用例编号:%s,执行状态为No,故不执行。" % (caseid))
                        endonecasetime = time.time()
                        runonecasetime = round(endonecasetime - startonecasetime, 2)
                        savedata = "insert into automation_function_app  (`devicesinfos`,`appiumport`,`devicesexecute`,`operatetype`,`element`,`parameter`,`waittime`,`rundescribe`,`caseexecute`,`runcasetime`,`caseid`,`eventid`,`createdtime`,`updatetime`)VALUES('%s','%s','%s','%s',\"%s\",'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            devicesinfos, port, devicesexecute, operatetype, element, parameter, waittime, rundescribe,
                            caseexecute,
                            runonecasetime, caseid, eventid,
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                    if isquit == "open":
                        pass
                    else:
                        driver.quit()  # 关闭Appium的连接
                    endtimecasetime = time.time()  # 结束用例执行时间
                    runcasetime = round(endtimecasetime - startcasetime, 2)
                    print("第%s台设备:%s,执行用例时间为:%ss" % (i, deviceName, runcasetime))  # 计算执行用例运行时间
                    # except:
                    # driver.quit()
                    # print("请检查Appium和设备是否正常连接。")
                elif platformName == "IOS":
                    pass
                else:
                    print("当前系统名称输入错误，请输入正确的设备系统，Android或IOS。")
            else:
                print("设备%s,状态为不执行，故该设备上不运行用例。"%(deviceName))
                savedata = "insert into automation_function_app  (`devicesinfos`,`appiumport`,`devicesexecute`,`operatetype`,`element`,`parameter`,`waittime`,`rundescribe`,`caseexecute`,`runcasetime`,`caseid`,`eventid`,`createdtime`,`updatetime`)VALUES('%s','%s','%s','%s',\"%s\",'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    devicesinfos, port, devicesexecute, "", "", "", "", "",
                    "",
                    "", "", eventid,
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))


if __name__ == "__main__":
    FunctionAutomation().runTestCase("Noopen")
