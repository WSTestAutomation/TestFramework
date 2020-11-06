# coding=utf-8

import os
import sys
import logging
import yaml
from appium import webdriver
from ui.lib.base_device import *
from common.lib.base_config import UI_CONFIG_DIR


fwd_caps_path = os.path.join(UI_CONFIG_DIR, 'appium_caps.yaml')
with open(fwd_caps_path, 'r', encoding='utf-8') as file:
    caps_data = yaml.load(file, Loader=yaml.FullLoader)

def appium_ios_desired(caps):

    data = caps_data[caps]
    desired_caps = {
        "platformName": "ios",
        "platformVersion": get_device_version(),
        "deviceName": get_device_name(),
        "udid": get_device_udid(),
        "app": data["app"],
        "noReset": data["noReset"],
        "useNewWDA": False,
        "automationName": data["automationName"],
        "commandTimeouts": data["commandTimeouts"],
        "newCommandTimeout": data["newCommandTimeout"]
    }

    print(desired_caps)
    logging.info("Start APP.")

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(3)
    return driver


def appium_android_desired(caps):

    data = caps_data[caps]
    desired_caps = {
        "platformName": "android",
        "platformVersion": get_android_devices_version(),
        "deviceName": get_device_name(),
        "deviceId": get_android_devices_id(),
        #"app": data["app"],
        "appPackage": data["appPackage"],        
        "appActivity": data["appActivity"],
        "noReset": data["noReset"],
        "unicodeKeyboard": data["unicodeKeyboard"],
        "resetKeyboard": data["resetKeyboard"]
    }

    print(desired_caps)
    logging.info("Start APP.")

    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(3)
    return driver


if __name__ == '__main__':
    appium_android_desired('Android_BaiduMap')
