import time
from selenium import webdriver
# profile_dir = r'/Volumes/Mac/users/steel/Library/Application Support/Firefox/Profiles/aidkprvv.default'
# profile = webdriver.FirefoxProfile(profile_dir)
# driver = webdriver.Firefox(profile)
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").clear()
print("成功")
time.sleep(5)
# driver.find_element_by_id("kw").send_keys("123")
element = '''//*[@id="kw"]'''
driver.find_element_by_xpath(element).send_keys("2222")
driver.find_element_by_id("su").click()
print("成功")
time.sleep(5)
driver.close()
driver.quit()
driver = None
print("成功")