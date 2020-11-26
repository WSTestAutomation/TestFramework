# coding=utf-8
# @Time    :
# @Author  :
# @File    : base_web.py

import logging
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from ui.lib.browser_engine import Logger, web_config_path, web_config

timeout_webdriverwait = web_config['implicitly_wait']

class BaseWebPage(object):

    def __init__(self, driver):
        self.driver = driver

    def quit_browser(self):
        logging.info('关闭浏览器')
        self.driver.quit()

    def click_back_button(self):
        logging.info('点击浏览器后退按钮')
        self.driver.back()

    def click_forward_button(self):
        logging.info('点击浏览器前进按钮')
        self.driver.forward()

    def click_refresh_button(self):
        logging.info('点击浏览器刷新按钮')
        self.driver.refresh()

    def find_element(self, *loc, timeout=timeout_webdriverwait):
        logging.info('通过 %s: %s 查找元素', loc[0], loc[1])
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator=loc))
        return element

    def find_elements(self, *loc, timeout=timeout_webdriverwait):
        logging.info('通过 %s: %s 查找元素', loc[0], loc[1])
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator=loc))
        return elements

    def find_element_by_text(self, loc, text):
        elements = self.find_elements(*loc)
        for element in elements:
            if text in element.text:
                return element

    def find_element_by_xpath(self, loc):
        logging.info('通过 Xpath: %s 查找元素', loc)
        element = self.driver.find_element_by_xpath(loc)
        return element

    def click(self, loc):
        element = self.find_element(*loc)
        element.click()
        logging.info('点击元素 %s: %s', loc[0], loc[1])
        time.sleep(1)

    def clicks(self, loc, index):
        element = self.find_elements(*loc)
        element[index].click()
        logging.info('点击元素 %s: %s, index %s', loc[0], loc[1], index)
        time.sleep(1)

    def double_click(self, loc):
        element = self.find_element(*loc)
        ActionChains(self.driver).double_click(element).perform()

    def find_element_click(self, loc, text):
        element = self.find_element_by_text(loc, text)
        element.click()

    def send_keys(self, loc, text, need_clear=False, need_enter=False):
        element = self.find_element(*loc)
        # element.click()
        if need_clear:
            logging.info('清除输入框内容')
            element.clear()
        logging.info('输入值 %s', text)
        element.send_keys(text)
        if need_enter:
            logging.info('输入回车键')
            element.send_keys(Keys.ENTER)

    def send_keys_by_index(self, loc, text, index, need_clear=False):
        element = self.find_elements(*loc)[index]
        element.click()
        if need_clear:
            logging.info('清除输入框内容')
            element.clear()
        logging.info('输入值 %s', text)
        element.send_keys(text)

    def switch_to_window(self, current_handle):
        self.driver.switch_to.window(current_handle)

    def switch_to_window_by_handle(self, title):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                break

    def switch_to_window_by_index(self, index):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def close_window_by_title(self, current_handle):
        all_handles = self.driver.window_handles
        for window in all_handles:
            if window != current_handle:
                self.driver.switch_to.window(window)
                self.driver.close()
        self.driver.switch_to.window(current_handle)

    def switch_to_frame(self, frame):
        self.driver.switch_to.frame(frame)

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_alert(self, timeout = timeout_webdriverwait):
        alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present(), message='No alert show')
        return alert

    @staticmethod
    def _select_options_by_value(element, option_value):
        logging.info('Select Option %s, option %s', element, option_value)
        Select(element).select_by_value(option_value)

    @staticmethod
    def _get_select_options(element):
        logging.info('获取下拉列表的所有值')
        return Select(element).options

    # 鼠标动作链
    def action_catena(self, element, types):
        if types == "悬停":
            logging.info('悬停 %s', element)
            ActionChains(self.driver).move_to_element(element).perform()
        elif types == "双击":
            logging.info('双击 %s', element)
            ActionChains(self.driver).double_click(element).perform()
        elif types == "右击":
            logging.info('右击 %s', element)
            ActionChains(self.driver).context_click(element).perform()

    # 点击坐标
    def action_coordinates(self, xoffset, yoffset):
        ActionChains(self.driver).move_by_offset(xoffset, yoffset).click().perform()

    def set_attribute(self, element, attribute_name, value):
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",
                                   element, attribute_name, value)

    def get_attribute_value(self, element):
        self.driver.execute_script("return arguments[0].value",
                                   element)

    def remove_attribute(self, element, attribute_name):
        self.driver.execute_script("arguments[0].removeAttribute(arguments[1])",
                                   element, attribute_name)

    # 点击遮挡元素
    def perform_javascript_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_element_present(self, loc):
        try:
            self.driver.find_element(*loc)
        except NoSuchElementException:
            logging.info('未找到元素')
            return False
        return True

    def is_element_clickable(self, loc, timeout=1):
        if self.is_element_present(loc):
            try:
                # 已确认元素存在，减少等待时间。
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator=loc))
            except TimeoutException:
                logging.info('元素存在但无法点击。可能被遮挡。')
                return False
            return True
