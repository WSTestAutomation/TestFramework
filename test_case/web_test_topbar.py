# coding=utf-8

import sys
import os
sys.path.append(os.path.dirname(os.getcwd())+os.path.sep+".")
sys.path.append(os.getcwd())

import time
import unittest
from businessview.web.common.login_business import simple_login
from businessview.web.common.stream_topbar_business import *
from utilstest.base_runner import BaseWebTestCase
from utilstest.base_yaml import Yaml
from common.browser_engine import Logger


class web_test(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
        self.data = Yaml(Yaml.web_config_path).read()
        self.env = self.data['env']
        self.homeUrl = self.data['portal'][self.env].rstrip("/")

    def test_mainpage(self):
        self.driver = simple_login()
        stream_topbar_business = Stream_topbar_business(self.driver)

        # home button
        stream_topbar_business.click_topbar_button_home()
        self.assertTrue(self.driver.current_url.rstrip("/") == self.homeUrl, '正在浏览主页')

        # discover button
        stream_topbar_business.click_topbar_button_discover()
        # TODO: wrap get_attribute from here to buissness.py
        #self.assertTrue(stream_topbar_business.discover_button_element.get_attribute("aria-expanded") == 'true', '展开discover菜单')
        #self.assertTrue(stream_topbar_business.discover_dropmenu_element.get_attribute("aria-hidden") == 'false', '显示discover菜单')
        stream_topbar_business.click_topbar_button_discover()
        #self.assertTrue(stream_topbar_business.discover_button_element.get_attribute("aria-expanded") == 'false', '收起discover菜单')
        #self.assertTrue(stream_topbar_business.discover_dropmenu_element.get_attribute("aria-hidden") == 'true', '隐藏discover菜单')
        stream_topbar_business.click_topbar_button_discover()
        #self.assertTrue(stream_topbar_business.discover_button_element.get_attribute("aria-expanded") == 'true', '展开discover菜单')
        #self.assertTrue(stream_topbar_business.discover_dropmenu_element.get_attribute("aria-hidden") == 'false', '显示discover菜单')
        stream_topbar_business.click_topbar_button_home()
        self.assertTrue(self.driver.current_url.rstrip("/") == self.homeUrl, '正在浏览主页')
        #self.assertTrue(stream_topbar_business.discover_button_element.get_attribute("aria-expanded") == 'false', '收起discover菜单')
        #self.assertTrue(stream_topbar_business.discover_dropmenu_element.get_attribute("aria-hidden") == 'true', '隐藏discover菜单')

        # discover menu
        stream_topbar_business.click_topbar_button_home()
        self.assertTrue(self.driver.current_url.rstrip("/") == self.homeUrl, '正在浏览主页')
        for it in stream_topbar_business.discover_dropdown_menu_dict:
            stream_topbar_business.click_topbar_button_discover()
            self.assertTrue(stream_topbar_business.discover_button_element.get_attribute("aria-expanded") == 'true', '展开discover菜单')
            self.assertTrue(stream_topbar_business.discover_dropmenu_element.get_attribute("aria-hidden") == 'false', '显示discover菜单')
            menu_link_element = stream_topbar_business.find_element(*stream_topbar_business.discover_dropdown_menu_dict[it])
            expect_url = menu_link_element.get_attribute("href")
            stream_topbar_business.click_topbar_link(stream_topbar_business.discover_dropdown_menu_dict[it])
            self.assertTrue(self.driver.current_url.rstrip("/") == expect_url, '正在浏览 ' + expect_url)
            stream_topbar_business.click_topbar_button_home()
            self.assertTrue(self.driver.current_url.rstrip("/") == self.homeUrl, '正在浏览主页')
        
        # dicover video link
        stream_topbar_business.click_topbar_button_discover()
        stream_topbar_business.click_topbar_link(stream_topbar_business.discover_dropdown_menu_dict['Videos'])
        
if __name__ == '__main__':
    unittest.main()
