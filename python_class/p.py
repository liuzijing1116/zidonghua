from selenium import webdriver
import time
driver = webdriver.Chrome(r'C:\zidonghua\chromedriver.exe')
driver.implicitly_wait(5)
driver.get("http://erp.lemfix.com/")
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()
driver.find_element_by_xpath("//span[text()='零售出库']").click()
P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
F_id = P_id + "-frame"
driver.switch_to.frame(F_id)
driver.find_element_by_id("searchNumber").send_keys("8621")
driver.find_element_by_id("searchBtn").click()
time.sleep(2)
num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
print(num)