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

    @BeautifulReport.add_test_img('test_manage_deleted_users-test_1-screenshot1')
    def test_admin_page(self):
        self.driver = simple_login()
        self._testMethodDoc = "Validate admin navigation"
        manage_del_user = Manage_deleted_users_business(self.driver)

        manage_del_user.click_settings()

        manage_del_user.click_admin_link()

    
        # if self.assertTrue(self.driver.current_url.endswith('/admin?view=Administrators')):
        #     time.sleep(5)
        manage_del_user.admin_settings_page()
        
            

        self.save_img("test_manage_deleted_users-test_1-screenshot1")
        

if __name__ == '__main__':
    unittest.main()
