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

    # 双击操作
    def operateDoubleClick(self, operatetype, element, driver, caseid):
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

    # 右点击击操作
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
        # 扩展性 查找元素方法
        elif operatetype == "点击_cssid":
            try:
                driver.find_element_by_css_selector("#%s" % (element)).click()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "点击_cssname":
            try:
                driver.find_element_by_css_selector("a[name=\"%s\"]" % (element)).click()
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

        # 扩展性 查找元素方法
        elif operatetype == "输入_cssid":
            try:
                driver.find_element_by_css_selector("#%s" % (element)).send_keys(parameter[0])
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "输入_cssname":
            try:
                driver.find_element_by_css_selector("a[name=\"%s\"]" % (element)).send_keys(parameter[0])
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        else:
            casereport = "用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid)
            return casereport

            # Android物理按键操作

    def operatePhysicsKye(self, operatetype, element, driver, caseid):
        if operatetype == "按enter_id":
            try:
                driver.find_element_by_id(element).send_keys(Keys.ENTER)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "按enter_xpath":
            try:
                driver.find_element_by_xpath(element).send_keys(Keys.ENTER)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "按enter_textname":
            try:
                driver.find_elements_by_name(element)[0].send_keys(Keys.ENTER)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "pagedown_id":
            try:
                driver.find_element_by_id(element).send_keys(Keys.PAGE_DOWN)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "pagedown_xpath":
            try:
                driver.find_element_by_xpath(element).send_keys(Keys.PAGE_DOWN)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "pagedown_textname":
            try:
                driver.find_elements_by_name(element)[0].send_keys(Keys.PAGE_DOWN)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "pageup_id":
            try:
                driver.find_element_by_id(element).send_keys(Keys.PAGE_UP)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "pageup_xpath":
            try:
                driver.find_element_by_xpath(element).send_keys(Keys.PAGE_UP)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "pageup_textname":
            try:
                driver.find_elements_by_name(element)[0].send_keys(Keys.PAGE_UP)
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "浏览器全屏":
            try:
                driver.maximize_window()
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        elif operatetype == "设置分辨率":
            try:
                windowslist = element.split(',')
                driver.set_window_size(int(windowslist[0]), int(windowslist[1]))
                casereport = "用例编号:%s,执行通过。" % (caseid)
                return casereport
            except:
                casereport = "用例编号:%s,执行不通过。" % (caseid)
                return casereport
        else:
            casereport = "用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid)
            return casereport

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
            eventid = time.strftime('%Y%m%d%H%M%S', time.localtime())
            if "Y" in browserstatus:
                driver = WebAutomation().startBrowser(browsername, browserconfigure)
                time.sleep(5)
                driver.get(testurl)
                casedata = launchTime.ReadExcel().readeExcelData('browseefuncase')  # 读取自动化用例数据
                x = 1
                try:
                    startonecasetime = time.time()
                    while x < casedata.get('caserows'):
                        excelcasedata = casedata.get('excledata_sheel').row_values(x)
                        x = x + 1
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
                            elif operatetype == "点击_cssid":
                                print(WebAutomation().operateClick(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "点击_cssname":
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
                            elif operatetype == "输入_cssid":
                                print(WebAutomation().operateInput(operatetype, element, driver, caseid, parameter))
                                time.sleep(waittime)
                            elif operatetype == "输入_cssname":
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
                            elif operatetype == "按enter_id":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "按enter_xpath":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "按enter_textname":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "pagedown_id":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "pagedown_xpath":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "pagedown_textname":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "pageup_id":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "pageup_xpath":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "pageup_textname":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "浏览器全屏":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            elif operatetype == "设置分辨率":
                                print(WebAutomation().operatePhysicsKye(operatetype, element, driver, caseid))
                                time.sleep(waittime)
                            else:
                                casereport = "用例编号:%s操作类型错误,该用例不执行。" % (caseid)
                                print(casereport)
                        else:
                            casereport = "用例编号:%s,执行状态为No,故不执行。" % (caseid)
                            print(casereport)
                        endonecasetime = time.time()
                        runonecasetime = round(endonecasetime - startonecasetime, 2)
                        savedata = "insert into automation_function_web  (`browsername`,`browserconfigure`,`browserstatus`,`operatetype`,`element`,`parameter`,`waittime`,`rundescribe`,`caseexecute`,`runcasetime`,`caseid`,`eventid`,`casereport`,`createdtime`,`updatetime`)VALUES('%s','%s','%s','%s',\"%s\",'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                            browsername, browserconfigure, browserstatus, operatetype, element, parameter, waittime,
                            rundescribe,
                            caseexecute,
                            runonecasetime, caseid, eventid, casereport,
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                        try:
                            launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                        except:
                            print("数据库连接失败，保存数据失败。")

                except:
                    driver.close()
                    driver.quit()
                driver.close()
                driver.quit()
            else:
                print("浏览%s,状态为不执行，故该浏览器上不运行用例。" % (devicesinfocase[0]))
                savedata = "insert into automation_function_web  (`browsername`,`browserconfigure`,`browserstatus`,`operatetype`,`element`,`parameter`,`waittime`,`rundescribe`,`caseexecute`,`runcasetime`,`caseid`,`eventid`,`casereport`,`createdtime`,`updatetime`)VALUES('%s','%s','%s','%s',\"%s\",'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
                    browsername, browserconfigure, browserstatus, "", "", "", "",
                    "",
                    "",
                    "", "", eventid, casereport,
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                try:
                    launchTime.MysqlConnect().saveDatatoMysql("%s" % (savedata))
                except:
                    print("数据库连接失败，保存数据失败。")


if __name__ == "__main__":
    WebAutomation().runCase()
