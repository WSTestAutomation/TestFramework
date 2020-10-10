# coding=utf-8

import os
import sys
import yaml
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from utilstest.base_log import Log
from selenium.webdriver import DesiredCapabilities
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
Logger = Log().get_logger()

base_dir = os.path.dirname(os.path.dirname(__file__))
if sys.platform.__eq__('win32'):
    chrome_driver_path = os.path.join(base_dir, 'drivers', 'chromedriver.exe')
    msedge_driver_path = os.path.join(base_dir, 'drivers', 'msedgedriver.exe')
    ie_driver_path = os.path.join(base_dir, 'drivers', 'IEDriverServer.exe')
    firefox_driver_path = os.path.join(base_dir, 'drivers', 'firefoxdriver.exe')
elif sys.platform.__eq__('darwin'):
    chrome_driver_path = os.path.join(base_dir, 'drivers', 'chromedriver')


def open_browser(env, browser='chrome'):    
    driver = None
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    if browser == "msedge":
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument('-inprivate')
        driver = Edge(executable_path=msedge_driver_path, options=edge_options)
    if browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--incognito')
        driver = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options)
    elif browser == "ie":
        driver = webdriver.Ie(executable_path=ie_driver_path)
        # selenium grid
        # driver = webdriver.Remote(command_executor='http://10.22.40.234:5555/wd/hub',
        #                           desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)

    # 获取web配置文件
    web_config_path = os.path.join(base_dir, 'config/web_config.yaml')
    with open(web_config_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    if env == "msit":
        url = data["portal"]['msit']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    if env == "srol1":
        url = data["portal"]['srol1']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    if env == "srol2":
        url = data["portal"]['srol2']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    if env == "ppe":
        url = data["portal"]['ppe']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    if env == "refe":
        url = data["portal"]['refe']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    elif env == '':
        driver = None
    driver.maximize_window()
    driver.implicitly_wait(data['implicitly_wait'])
    return driver


if __name__ == "__main__":
    web_driver = open_browser(env='url')
    web_driver.close()
    web_driver.quit()
