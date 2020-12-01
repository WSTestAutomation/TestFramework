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


class web_test_manage_delete_user(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
        self.data = Yaml(web_config_path).read()
        self.env = self.data['env']
        self.homeUrl = self.data['portal'][self.env].rstrip("/")

    # @BeautifulReport.add_test_img('test_manage_deleted_users-test_1-screenshot1')
    def test_admin_page(self):
        self.driver = simple_login()

        manage_del_user = Manage_deleted_users_business(self.driver)

        manage_del_user.click_admin_link()

        # 获取页面标题
        title = self.driver.title

        self.assertEqual(title, "Admin settings | Microsoft Stream", "当前在admin settings页面")

        manage_del_user.admin_settings_page()
        
        manage_del_user.search('test')

        manage_del_user.icon_edit()
        manage_del_user.edit_user_details("test video")
        
        
        # self.save_img("test_manage_deleted_users-test_1-screenshot1")
        
if __name__ == "__main__":
    unittest.main()
    
