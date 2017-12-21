from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.yimi.student.mobile'
desired_caps['appActivity'] = 'com.yimi.student.activity.WelcomeActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
print(x,y)
#driver.find_element_by_name("1").click()
driver.quit()