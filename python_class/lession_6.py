from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

# driver = webdriver.Chrome(r'C:\zidonghua\chromedriver.exe')
# driver.implicitly_wait(5)
# driver.get("http://http://erp.lemfix.com/")


def login_page(username, password, driver):  # 登录
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()


def open_url(url, driver):  # 打开网页
    driver.get(url)
    driver.maximize_window()


def search_key(url, username, password, driver, s_key):
    open_url(url, driver)
    login_page(username, password, driver)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    F_id = P_id + "-frame"
    driver.switch_to.frame(F_id)
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(2)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num


