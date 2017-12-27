from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['udid'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.ushaqi.zhuishushenqi'
desired_caps['appActivity'] = 'com.ushaqi.zhuishushenqi.ui.SplashActivity'

driver = webdriver.Remote('http://localhost:4726/wd/hub', desired_caps)
time.sleep(5)
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
print(x,y)
driver.find_element_by_id("com.ushaqi.zhuishushenqi:id/btnEntryApp").click()
#driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.ushaqi.zhuishushenqi:id/home_action_menu_more']").click()
driver.find_element_by_name(u"去添加").click()
driver.quit()