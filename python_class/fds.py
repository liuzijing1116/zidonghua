from selenium import webdriver
import time

wd = webdriver.Chrome(r'C:\zidonghua\chromedriver.exe')
wd.implicitly_wait(5)
# wd.get('http://erp.lemfix.com')
wd.get('https://www.zhihu.com/')
# 窗口最大化
wd.maximize_window()
# time.sleep(2)
# # 向前 退后 刷新
# wd.back()  # 退后
# time.sleep(2)
# wd.forward()  # 向前
# time.sleep(2)
# wd.refresh()  # 刷新
# time.sleep(2)
# 退出
# wd.quit()  # 关闭驱动
# wd.close()  # 关闭当前窗口，不关闭会话
# 元素定位： id  name xpath
# 1.绝对路径/相对路径   //input[@id="username"]   xpath表达方式     //标签名+属性值 = //标签名[@属性名=属性值]
# 2.层级定位方式       //div[@class="login-info"]//b              //标签名[@属性值]//标签名[@属性名=属性值]
# 3.文本属性定位       //div[text()="密码登录"]                    //   text()   可以赋值为一个变量，变成文本形式
# 4.包含属性值          //div[contains(@class,"SignFlow-tab SignFlow-tab--active")]     //标签名[contains(@属性名/text(),属性值)]
page = wd.find_element_by_xpath('//div[@class="SignFlow-tab SignFlow-tab--active"]').text
print(page)
time.sleep(2)
# send_keys() 输入框输入值
wd.find_element_by_name("username").send_keys("15712574997")
# 等待 3种方式
# time.sleep()  wd.implicitly_wait(5)  expected_dondition
page_title = wd.title  # 获取页面标题
# 识别是否有子页面的方式： 页面层级路径里出现iframe：需要切换iframe才能进行元素定位
# 切换iframe
# 1.找到iframe元素,通过id进行切换。//div[text()='零售出库']/..    可以找到上一层元素，然后通过.get_attribute(id)方法获取id，赋值给一个变量a，再去拼接得到b，b就是id。
# wd.switch_to.frame(b )
# 2.通过元素定位（xpath）切换frame
# wd.switch_to.frame(wd.find_element_by_xpath("//iframe[@id='{}']".format(b)))
# 3.通过iframe下标   去看html标签，第一个html为0，以此类推
# wd.switch_to.frame(1)
wd.find_element_by_id()