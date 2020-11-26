# coding=utf-8

import os
import sys
import yaml
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from common.lib.base_log import Log
from common.lib.base_config import UI_OUTPUT_DIR, UI_DRIVERS_DIR, UI_CONFIG_DIR
from selenium.webdriver import DesiredCapabilities

ui_log_dir = os.path.join(UI_OUTPUT_DIR, 'logs')
Logger = Log(ui_log_dir).get_logger() # 初始化日志模块
# 获取web配置
web_config_path = os.path.join(UI_CONFIG_DIR, 'web_config.yaml')
with open(web_config_path, 'r', encoding='utf-8') as file:
    web_config = yaml.load(file, Loader=yaml.FullLoader)

if sys.platform.__eq__('win32'):
    chrome_driver_path = os.path.join(UI_DRIVERS_DIR, 'chromedriver.exe')
    msedge_driver_path = os.path.join(UI_DRIVERS_DIR, 'msedgedriver.exe')
    ie_driver_path = os.path.join(UI_DRIVERS_DIR, 'IEDriverServer.exe')
    firefox_driver_path = os.path.join(UI_DRIVERS_DIR, 'firefoxdriver.exe')
elif sys.platform.__eq__('darwin'):
    chrome_driver_path = os.path.join(UI_DRIVERS_DIR, 'chromedriver')


def open_browser(env, browser='chrome', incognito=True):
    driver = None
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if incognito:
            chrome_options.add_argument('--incognito')
        driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    elif browser == "msedge":
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        if incognito:
            edge_options.add_argument('-inprivate')
        driver = Edge(executable_path=msedge_driver_path, options=edge_options)
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if incognito:
            firefox_options.add_argument('--incognito')
        driver = webdriver.Firefox(executable_path=firefox_driver_path, options=firefox_options)
    elif browser == "ie":
        driver = webdriver.Ie(executable_path=ie_driver_path)
        # selenium grid
        # driver = webdriver.Remote(command_executor='http://10.22.40.234:5555/wd/hub',
        #                           desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
    elif browser == "safari":
        driver = webdriver.Safari()

    # 以下是一个示例，基于config/web_config.yaml文件做的配置
    if env == "msit":
        url = web_config["portal"]['msit']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    if env == "srol1":
        url = web_config["portal"]['srol1']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    if env == "srol2":
        url = web_config["portal"]['srol2']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    if env == "ppe":
        url = web_config["portal"]['ppe']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    if env == "refe":
        url = web_config["portal"]['refe']
        Logger.info("Open Url: %s", url)
        driver.get(url)
    elif env == '':
        driver = None
    driver.maximize_window()
    driver.implicitly_wait(web_config['implicitly_wait'])
    return driver


if __name__ == "__main__":
    web_driver = open_browser(env='url')
    web_driver.close()
    web_driver.quit()
