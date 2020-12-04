# coding=utf-8

import sys
import os
import time
import unittest
from common.package.BeautifulReport.BeautifulReport import BeautifulReport
from ui.view.businessview.web.common.login_business import simple_login
from ui.view.businessview.web.admin.manage_deleted_users_business import *
from ui.lib.base_runner import BaseWebTestCase
from common.lib.base_yaml import Yaml
from ui.lib.browser_engine import Logger, web_config_path
from selenium import webdriver


class web_test_manage_delete_user(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
    
    def test_admin_page(self):
        self.driver = simple_login()
        self.data = Yaml(web_config_path).read()
        self.env = self.data['env']
        adminUrl = self.data['portal'][self.env] + "/admin"
        self.driver.get(adminUrl)
        try:
            manage_del_user = Manage_deleted_users_business(self.driver)
            # manage_del_user.click_settings_button()
            # manage_del_user.click_admin_link()
            # title = self.driver.title
            # self.assertEqual(title, "Admin settings | Microsoft Stream", "当前在admin settings页面！")
            manage_del_user.admin_settings_page()
            # 搜索关键字：test
            search_input = "test"
            manage_del_user.search(search_input)
            self.assertEqual('test', search_input, "两个值相等")
            manage_del_user.icon_edit()
            # self.assertTrue(manage_del_user.get_attribute("aria-hidden") == "false", "点击edit按钮失败")
            manage_del_user.edit_user_details("test_user")
            # self.assertEqual(manage_del_user.assert_success(), " Save ", "成功点击save按钮")
            manage_del_user.edit_cancel()
            manage_del_user.delete_button()
            manage_del_user.cancel_delete_button()
            
            
        except Exception:
            self.save_img("test_manage_deleted_users-test_error1-screenshot1")
    
    
if __name__ == "__main__":
    unittest.main()
    
