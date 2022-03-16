from selenium import webdriver
from python_class import lession_6
from test_data import test_data

driver = webdriver.Chrome(r'C:\zidonghua\chromedriver.exe')
driver.implicitly_wait(10)
# 调用函数
url = test_data.url.get("url")  # 取url
name = test_data.login_num.get("username")
pwd = test_data.login_num.get("password")
s_key = test_data.s_key.get("s_key")
# print(url, name, pwd, s_key)
result = lession_6.search_key(driver=driver, url=url, username=name, password=pwd, s_key=s_key)
if s_key in result:
    print("搜索结果正确")
else:
    print("用例测试不通过")
