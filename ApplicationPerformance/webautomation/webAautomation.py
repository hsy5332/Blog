import time
import applicationperformance.launchTime as launchTime  # MAC
# import ApplicationPerformance.applicationperformance.launchTime as launchTime  # Windows

from selenium import webdriver


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

    # 点击操作
    def operateClick(self, operatetype, element, driver, caseid):
        if operatetype == "点击_id":
            try:
                driver.find_element_by_id(element).click()
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))

        elif operatetype == "点击_xpath":
            try:
                driver.find_element_by_xpath(element).click()
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))

        elif operatetype == "点击_textname":  # 点击textname
            try:
                driver.find_elements_by_name(element)[0].click()  # 这里有问题
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))

        elif operatetype == "点击_classname":
            try:
                driver.find_elements_by_class_name(element)[0].click()  # 点击xpath
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        elif operatetype == "点击_linkname":
            try:
                driver.find_elements_by_link_text(element)[0].click()
                print("用例编号:%s,执行通过。" % (caseid))
            except:
                print("用例编号:%s,执行不通过。" % (caseid))
        else:
            print("用例编号:%s,执行不通过，该用例的元素属性或参数可能有问题，请检查该用例。" % (caseid))

    # 检查元素是否存在
    def operateCheckElement(self):
        pass

    # 输入操作
    def operateInput(self):
        pass

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
                    caseid = int(excelcasedata[0])  # 用例编号
                    operatetype = excelcasedata[1]  # 操作类型
                    element = excelcasedata[2]  # 元素
                    parameter = excelcasedata[3]  # 参数
                    rundescribe = excelcasedata[6]  # 步骤描述
                    caseexecute = excelcasedata[7]  # 用例状态
                    if excelcasedata[5] == "":  # 等待时间
                        waittime = 2
                    else:
                        waittime = int(excelcasedata[5])
                    if "Y" in caseexecute:
                        if operatetype == "等待时间":
                            time.sleep(waittime)
                            print("用例编号:%s,执行通过。" % (caseid))
                        elif operatetype == "点击_id":
                            WebAutomation().operateClick(operatetype, element, driver, caseid)
                            time.sleep(waittime)
                        elif operatetype == "点击_xpath":
                            WebAutomation().operateClick(operatetype, element, driver, caseid)
                            time.sleep(waittime)
                        elif operatetype == "点击_textname":
                            # driver.find_element_by_id("kw").send_keys("事实上")
                            WebAutomation().operateClick(operatetype, element, driver, caseid)
                            time.sleep(waittime)
                        elif operatetype == "点击_linkname":
                            WebAutomation().operateClick(operatetype, element, driver, caseid)
                            time.sleep(waittime)
                        elif operatetype == "点击_classname":
                            WebAutomation().operateClick(operatetype, element, driver, caseid)
                            time.sleep(waittime)
                        else:
                            print("用例编号:%s操作类型错误,该用例不执行。" % (caseid))
                    else:
                        print("用例编号:%s,执行状态为No,故不执行。" % (caseid))
                    x = x + 1
                driver.close()
                driver.quit()



            else:
                print("浏览%s,状态为不执行，故该浏览器上不运行用例。" % (devicesinfocase[0]))


WebAutomation().runCase()
