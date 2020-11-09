# coding=utf-8
# @Time :
# @Author :
# @File : base_app.py

import time
import logging
from appium.webdriver.common.mobileby import MobileBy, By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BaseAppPage(object):
    btn = (MobileBy.IOS_PREDICATE, 'label=="隐藏键盘"')

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc, time_=5):
        logging.info('通过 %s: %s 查找元素', loc[0], loc[1])
        element = WebDriverWait(self.driver, time_).until(EC.presence_of_element_located(locator=loc))
        return element

    def find_elements(self, *loc, time_=5):
        logging.info('过 %s: %s 查找元素', loc[0], loc[1])
        elements = WebDriverWait(self.driver, time_).until(EC.presence_of_all_elements_located(locator=loc))
        return elements

    def get_attribute(self, loc, name):
        element = self.find_element(*loc)
        logging.info('获取元素的属性值 %s', name)
        return element.get_attribute(name)

    def click(self, loc):
        element = self.find_element(*loc)
        logging.info('点击元素 %s: %s', loc[0], loc[1])
        element.click()
        time.sleep(1)

    def clicks(self, loc, index):
        elements = self.find_elements(*loc)
        logging.info('点击元素 %s: %s, index %s' , loc[0], loc[1], index)
        elements[index].click()
        time.sleep(1)

    def send_keys(self, loc, text, need_clear=False, need_hide_keyboard=False):
        element = self.find_element(*loc)
        element.click()
        if need_clear:
            logging.info('清除输入框已存在的内容')
            element.clear()
        logging.info('输入值 %s', text)
        element.set_value(text)
        if need_hide_keyboard:
            logging.info('隐藏输入键盘')
            self.click(self.btn)

    def set_value_by_index(self, loc, text, index):
        element = self.find_elements(*loc)[index]
        element.click()
        logging.info('输入值 %s', text)
        element.set_value(text)
        self.click(self.btn)

    def get_window_size(self):
        """获取屏幕的高度和宽度"""
        height = self.driver.get_window_size()['height']
        width = self.driver.get_window_size()['width']
        return height, width

    def get_element_rect(self, loc):
        element = self.find_element(*loc)
        return element.rect

    def touch_element_by_position(self, loc, index=0):
        element = self.find_elements(*loc)[index]
        x = element.rect['x'] + (element.rect['width'] / 2)
        y = element.rect['y'] + (element.rect['height'] / 2)
        TouchAction(self.driver).tap(x=x, y=y).perform()
        time.sleep(1)

    def swipe_select_time(self, loc, start_time, end_time):
        elements = self.find_elements(*loc)
        element_rect = elements[-1].rect

        element_x = element_rect['x']
        element_y = element_rect['y']
        element_height = element_rect['height']

        end_y = element_y + element_height

        if start_time > end_time:
            times = int(start_time) - int(end_time)
            for _ in range(times):
                self.drag_from_to_duration(element_x, element_y, element_x, end_y, 0.5)

        elif start_time < end_time:
            times = int(end_time) - int(start_time)
            for _ in range(times):
                self.drag_from_to_duration(element_x, end_y, element_x, element_y, 0.3)

    def drag_from_to_duration(self, start_x, start_y, end_x, end_y, duration=None):
        """
        drag from to duration
        :param start_x: x-coordinate at which to start
        :param start_y: y-coordinate at which to start
        :param end_x: x-coordinate at which to stop
        :param end_y: y-coordinate at which to stop
        :param duration: time to take the swipe, in ms
        :return:
        """
        self.driver.execute_script("mobile:dragFromToForDuration", {"duration": duration, "element": None,
                                                                    "fromX": start_x, "fromY": start_y, "toX": end_x,
                                                                    "toY": end_y})

    def _find_element(self, *loc, time_=5):
        logging.info('通过 %s: %s 查找元素', loc[0], loc[1])
        element = WebDriverWait(self.driver, time_).until(EC.presence_of_element_located(locator=loc))
        return element

    def _find_elements(self, *loc, time_=5):
        logging.info('通过 %s: %s 查找元素', loc[0], loc[1])
        elements = WebDriverWait(self.driver, time_).until(EC.presence_of_all_elements_located(locator=loc))
        return elements
