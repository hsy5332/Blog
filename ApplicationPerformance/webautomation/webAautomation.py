# to do 发送邮件，以及需要增加用例的执行结果
import time
import applicationperformance.launchTime as launchTime  # MAC
# import ApplicationPerformance.applicationperformance.launchTime as launchTime  # Windows

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class WebAutomation(object):
    # 启动浏览
    def startBrowser(self, browsername, testurl, *browserconfigure):
        if "谷歌" in browsername:
            driver = webdriver.Chrome()
            return driver
        elif "火狐" in browsername:
            if browserconfigure[0] != "":  # 判断是否有配置路径
                driver = webdriver.Firefox(webdriver.FirefoxProfile(browserconfigure[0]))  # 带着配置启动火狐浏览器（比如增加Xpth插件等。）
                return driver
            else:
                driver = webdriver.Firefox()
                return driver
        else:
            print("您的测试用例中，存在无法识别的浏览器名称，请检查用例。")
    #双击操作
    def operateDoubleClick(self,operatetype, element, driver, caseid):
        if operatetype == "双击_id":
            try:
                driver.find_element_by_id(element).double_click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "双击_xpath":
            try:
                driver.find_element_by_xpath(element).double_click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "双击_textname":  # 点击textname
            try:
                driver.find_elements_by_name(element)[0].double_click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "双击_classname":
            try:
                driver.find_elements_by_class_name(element)[0].double_click()  # 点击xpath
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "双击_linkname":
            try:
                driver.find_elements_by_link_text(element)[0].double_click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        else:
            casereport = "用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid)
            return casereport
    #右点击击操作
    def operateRightClick(self, operatetype, element, driver, caseid):
        if operatetype == "右击_id":
            try:
                driver.find_element_by_id(element).context_click().perform()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "右击_xpath":
            try:
                driver.find_element_by_xpath(element).context_click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "右击_textname":  # 点击textname
            try:
                driver.find_elements_by_name(element)[0].context_click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "右击_classname":
            try:
                driver.find_elements_by_class_name(element)[0].context_click()  # 点击xpath
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "右击_linkname":
            try:
                driver.find_elements_by_link_text(element)[0].context_click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        else:
            casereport = "用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid)
            return casereport
    # 左点击击操作
    def operateClick(self, operatetype, element, driver, caseid):
        if operatetype == "点击_id":
            try:
                driver.find_element_by_id(element).click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "点击_xpath":
            try:
                driver.find_element_by_xpath(element).click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "点击_textname":  # 点击textname
            try:
                driver.find_elements_by_name(element)[0].click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "点击_classname":
            try:
                driver.find_elements_by_class_name(element)[0].click()  # 点击xpath
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "点击_linkname":
            try:
                driver.find_elements_by_link_text(element)[0].click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        else:
            casereport = "用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid)
            return casereport

    # 检查元素是否存在
    def operateCheckElement(self, operatetype, element, driver, caseid):
        if operatetype == "查找_id":
            try:
                driver.find_element_by_id(element)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "查找_xpath":
            try:
                driver.find_element_by_xpath(element)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "查找_textname":  # 查找textname
            try:
                driver.find_elements_by_name(element)[0]
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport

        elif operatetype == "查找_classname":
            try:
                driver.find_elements_by_class_name(element)[0]
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "查找_linkname":
            try:
                driver.find_elements_by_link_text(element)[0]
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        else:
            casereport = "用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid)
            return casereport

    # 清空输入框
    def clearInput(self, operatetype, element, driver, caseid):
        if operatetype == "清空输入框_id":
            try:
                driver.find_element_by_id(element).clear()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "清空输入框_xpath":
            try:
                driver.find_element_by_xpath(element).clear()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "清空输入框_textname":
            try:
                driver.find_elements_by_name(element)[0].clear()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        else:
            casereport = "用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid)
            return casereport

    # 输入操作
    def operateInput(self, operatetype, element, driver, caseid, *parameter):
        if operatetype == "输入_id":
            try:
                driver.find_element_by_id(element).send_keys(parameter[0])
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "输入_xpath":
            try:
                driver.find_element_by_xpath(element).send_keys(parameter[0])
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "输入_textname":
            try:
                driver.find_elements_by_name(element)[0].send_keys(parameter[0])
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        else:
            casereport = "用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid)
            return casereport

        # Android物理按键操作
    def operatePhysicsKye(self, driver, caseid, *parameter):
        keycode = parameter[0]
        #try:
        driver.keyevent(keycode)
        casereport = "用例编号:%s,执行通过。" % (caseid)
        return casereport
        #except:
            #casereport = "用例编号:%s,执行不通过。" % (caseid)
            #return casereport
    # 执行用例
    def runCase(self):
        deviceinfo = launchTime.ReadExcel().readeExcelData('browserinfo')
        for i in range(1, deviceinfo.get('caserows')):
            devicesinfocase = deviceinfo.get('excledata_sheel').row_values(i)
            browsername = devicesinfocase[0]
            browserconfigure = devicesinfocase[1]
            testurl = devicesinfocase[2]
            browserstatus = devicesinfocase[3]
            print(devicesinfocase)
            if "Y" in browserstatus:
                driver = WebAutomation().startBrowser(browsername, browserconfigure)
                time.sleep(5)
                driver.get(testurl)
                casedata = launchTime.ReadExcel().readeExcelData('browseefuncase')  # 读取自动化用例数据
                x = 1
                while x < casedata.get('caserows'):
                    excelcasedata = casedata.get('excledata_sheel').row_values(x)
                    try:
                        caseid = int(excelcasedata[0])  # 用例编号
                    except:
                        caseid = excelcasedata[0]
                    operatetype = excelcasedata[1]  # 操作类型
                    element = excelcasedata[2]  # 元素
                    parameter = str(excelcasedata[3])  # 参数 必须要转成字符串，要不然在使用send_keys（必须要是字符串类型）时无法使用
                    rundescribe = excelcasedata[6]  # 步骤描述
                    caseexecute = excelcasedata[7]  # 用例状态
                    driver.implicitly_wait(60)
                    if excelcasedata[5] == "":  # 等待时间
                        waittime = 2
                    else:
                        waittime = int(excelcasedata[5])
                    if "Y" in caseexecute:
                        if operatetype == "等待时间":
                            time.sleep(waittime)
                            casereport = "用例编号:%s,执行通过。" % (caseid)
                            print(casereport)
                        elif operatetype == "点击_id":
                            print(WebAutomation().operateClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "点击_xpath":
                            print(WebAutomation().operateClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "点击_textname":
                            print(WebAutomation().operateClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "点击_linkname":
                            print(WebAutomation().operateClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "点击_classname":
                            print(WebAutomation().operateClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "输入_id":
                            print(WebAutomation().operateInput(operatetype, element, driver, caseid, parameter))
                            time.sleep(waittime)
                        elif operatetype == "输入_xpath":
                            print(WebAutomation().operateInput(operatetype, element, driver, caseid, parameter))
                            time.sleep(waittime)
                        elif operatetype == "输入_textname":
                            print(WebAutomation().operateInput(operatetype, element, driver, caseid, parameter))
                            time.sleep(waittime)
                        elif operatetype == "清空输入框_id":
                            print(WebAutomation().clearInput(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "清空输入框_xpath":
                            print(WebAutomation().clearInput(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "清空输入框_textname":
                            print(WebAutomation().clearInput(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "查找_id":
                            print(WebAutomation().operateCheckElement(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "查找_xpath":
                            print(WebAutomation().operateCheckElement(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "查找_textname":
                            print(WebAutomation().operateCheckElement(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "查找_linkname":
                            print(WebAutomation().operateCheckElement(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "查找_classname":
                            print(WebAutomation().operateCheckElement(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "右击_id":
                            print(WebAutomation().operateRightClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "右击_xpath":
                            print(WebAutomation().operateRightClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "右击_textname":
                            print(WebAutomation().operateRightClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "右击_linkname":
                            print(WebAutomation().operateRightClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "右击_classname":
                            print(WebAutomation().operateRightClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "双击_id":
                            print(WebAutomation().operateDoubleClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "双击_xpath":
                            print(WebAutomation().operateDoubleClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "双击_textname":
                            print(WebAutomation().operateDoubleClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "双击_linkname":
                            print(WebAutomation().operateDoubleClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "双击_classname":
                            print(WebAutomation().operateDoubleClick(operatetype, element, driver, caseid))
                            time.sleep(waittime)
                        elif operatetype == "物理按钮":
                            # try:
                            #     parameter = int(parameter)
                            # except:
                            #     parameter = 111 #如果物理按钮填写错误的话，给默认exc按钮
                            #     print("元素属性错误，已经使用默认的元素属性，请填写正确的")
                            # print(WebAutomation().operatePhysicsKye(driver, caseid, parameter))
                            print("进入。。。。")
                            driver.find_element_by_id("kw").send_keys(Keys.ENTER)
                            time.sleep(waittime)

                            print("111")
                        else:
                            casereport = "用例编号:%s操作类型错误,该用例不执行。" % (caseid)
                            print(casereport)
                    else:
                        casereport = "用例编号:%s,执行状态为No,故不执行。" % (caseid)
                        print(casereport)
                    x = x + 1
                driver.close()
                driver.quit()
            else:
                print("浏览%s,状态为不执行，故该浏览器上不运行用例。" % (devicesinfocase[0]))


WebAutomation().runCase()
