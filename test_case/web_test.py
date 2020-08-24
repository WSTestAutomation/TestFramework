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
from utilstest.base_yaml import Yaml
from common.browser_engine import Logger


class web_test(BaseWebTestCase):
    def __init__(self,*args,**kwargs):
        unittest.TestCase.__init__(self,*args,**kwargs)
        self.data = Yaml(Yaml.web_config_path).read()
        self.env = self.data['env']

    @BeautifulReport.add_test_img('web_test_login_{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_login(self):        
        Logger.info("Test Start:")
        Logger.info("Login to %s", self.env)
        self.driver = open_browser(self.env,'chrome')
        _loginBusiness = LoginBusiness(driver=self.driver)

        """
        # for SROL1 and SROL2, we can use test accounts
        _loginBusiness.login(self.data['user']['test1'], self.data['pwd']['commonpwd'])
        """
        # For PPE and MSIT, we can use our personal accounts.
        # MSIT may meet some additional steps for security reason which bloacks the test
        # PPE is much slower and need to wait for more seconds.
        _loginBusiness.login('Your Account', 'Your Password')

        Logger.info("Test End")
        
if __name__ == '__main__':
    unittest.main()

