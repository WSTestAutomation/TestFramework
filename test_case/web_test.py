# coding=utf-8

import sys
import os
sys.path.append(os.path.dirname(os.getcwd())+os.path.sep+".")
sys.path.append(os.getcwd())

import time
import unittest
from businessview.web.common.login_business import LoginBusiness
from BeautifulReport.BeautifulReport import BeautifulReport
from common.browser_engine import open_browser
from utilstest.base_runner import BaseWebTestCase


class web_test(BaseWebTestCase):

    @BeautifulReport.add_test_img('test_new_ai{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_new_ai(self):
        self.driver = open_browser('url')
        _loginBusiness = LoginBusiness(driver=self.driver)
        _loginBusiness.login()
        
if __name__ == '__main__':
    unittest.main()

