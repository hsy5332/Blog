import time
import ApplicationPerformance.applicationperformance.launchTime as launchTime
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'emulator-5556'
desired_caps['udid'] = 'emulator-5556'
desired_caps['appPackage'] = 'com.ushaqi.zhuishushenqi'
desired_caps['appActivity'] = 'com.ushaqi.zhuishushenqi.ui.SplashActivity'
# desired_caps['appPackage'] = 'sogou.mobile.explorer.speed'
# desired_caps['appActivity'] = 'sogou.mobile.explorer.NoDisplayActivity'

#driver = webdriver.Remote('http://localhost:4726/wd/hub', desired_caps)
# x = driver.get_window_size()['width']
# y = driver.get_window_size()['height']
# print(x, y)
#driver.find_element_by_id("com.ushaqi.zhuishushenqi:id/btnEntryApp").click()
# driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ushaqi.zhuishushenqi:id/home_action_menu_more']").click()
# try:
#     driver.find_element_by_id("com.ushaqi.zhuishushenqi:id/btnEntryApp").click()
#     driver.find_element_by_id("com.ushaqi.zhuishushenqi:id/home_action_menu_search").click()
#     #driver.find_elements_by_class_name("android.widget.EditText")[0].send_keys("123")
#     #print(driver.find_elements_by_class_name("android.widget.TextView"))
#     driver.find_elements_by_name("书名、作者、分类")[0].send_keys("12312")
#     driver.quit()
# except NoSuchElementException:
#     print("sss")
#     driver.quit()
#driver.find_element()

# driver.find_element_by_id("com.ushaqi.zhuishushenqi:id/home_action_menu_search").click()
casedata = launchTime.ReadExcel().readeExcelData('funcase')
endnumber = []
number =[]
for x in range(1, casedata.get('caserows')):  # Excel中的测试用例数据，使用for遍历每一行的数据，进行判断执行对应的操作
    excelcasedata = casedata.get('excledata_sheel').row_values(
        x)
    operatetype = excelcasedata[1]
    if operatetype == "if":
        number.append(x)
    if operatetype == "end":
        endnumber.append(x)
i = 1
ifnumber = 0
while i < casedata.get('caserows'):  # Excel中的测试用例数据，使用for遍历每一行的数据，进行判断执行对应的操作
    #print(i)
    excelcasedata = casedata.get('excledata_sheel').row_values(
        i)
    caseid = int(excelcasedata[0])  # 用例编号
    operatetype = excelcasedata[1]  # 操作类型
    element = excelcasedata[2]  # 元素属性
    parameter = excelcasedata[3]  # 参数（如：输入的数据）
    checkpoint = excelcasedata[4]  # 检查点对比
    # if operatetype == "if_":
    #     number = i
    # if operatetype == "end":
    #     endnumber = i
    i = i + 1
    if excelcasedata[5] == "":
        waittime = 2
    if "if包含_" in operatetype:
        if "com" in element:
            print(i, excelcasedata)
        else:
            print("执行失败")
            try:
                i = endnumber[ifnumber]
            except IndexError:
                pass
        ifnumber = ifnumber + 1
    elif operatetype == "end":
        print(i,"end")
    elif operatetype == "点击_textname":
        print(i,excelcasedata)
    elif operatetype == "物理按钮":
        print(i,excelcasedata)