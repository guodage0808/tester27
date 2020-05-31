import time
#使用ID定位
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(3)
driver.find_element_by_id("kw").send_keys("test")
time.sleep(2)
driver.find_element_by_id("su").click()
time.sleep(2)
driver.find_element_by_link_text("百度首页").click()
time.sleep(2)
driver.find_element_by_id("kw").click()
time.sleep(3)
driver.find_element_by_xpath("//form[@id='form']/div/ul/li/span").click()
print("123")