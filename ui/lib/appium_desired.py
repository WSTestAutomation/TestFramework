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

def get_desired_caps_data(caps):
    data = caps_data[caps]
    desired_caps = {}
    for (key, value) in data.items():
        desired_caps[key] = value

    desired_caps.pop('ip')
    desired_caps.pop('port')
    
    if data['platformName'].lower() == "android":
        desired_caps.update({
            "platformVersion": get_android_devices_version(),
            "deviceId": get_android_devices_id()
            })
    elif data['platformName'].lower() == "ios":
        desired_caps.update({
        "platformVersion": get_device_version(),
        "deviceName": get_device_name(),
        "udid": get_device_udid()
        })
    return desired_caps

def appium_desired(caps):

    data = caps_data[caps]
    desired_caps = get_desired_caps_data(caps)
    print(desired_caps)

    logging.info("Start APP.")
    driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
    driver.implicitly_wait(3)
    return driver


if __name__ == '__main__':
    appium_desired('android_baidumap')
