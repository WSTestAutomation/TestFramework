# coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver import DesiredCapabilities

def open_brower():
    driver = webdriver.Remote(command_executor='http://10.10.35.35:5555/wd/hub',
                          desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
    # print(driver)
    # 打开百度首页并搜索词语，最后判断搜索跳转页面标题是否含有搜索词
    wd = 'lovesoo'
    driver.get('https://www.baidu.com')
    time.sleep(5)
    driver.find_element_by_id("kw").send_keys(wd)
    driver.find_element_by_id("su").click()
    time.sleep(1)
    assert wd in driver.title, '{0} not in {1}'.format(wd, driver.title.encode('utf-8'))
    # driver.quit()


if __name__ == '__main__':
    open_brower()


# 定义node_hub与浏览器对应关系
# nodes = {
#     'http://127.0.0.1:5555/wd/hub': 'chrome',
#     'http://127.0.0.1:5556/wd/hub': 'internet explorer',
#     'http://127.0.0.1:5557/wd/hub': 'firefox'
# }
# 通过不同的浏览器执行测试脚本
# for host, browser in nodes.items():
#     print(host, browser)
#     # 调用remote方法
#     driver = Remote(command_executor=host,
#                     desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '', 'javascriptEnabled': True})