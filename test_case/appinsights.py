# coding=utf-8

import time
import unittest
from businessview.web.common.login_business import LoginBusiness
from businessview.web.appinsights_business import AiBusiness
from BeautifulReport.BeautifulReport import BeautifulReport
from common.browser_engine import open_browser
from utils.base_runner import BaseWebTestCase


class AppInsights(BaseWebTestCase):

    @BeautifulReport.add_test_img('test_new_ai{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_new_ai(self):
        """Create AI Automation Demo"""
        print("Login")
        self.driver = open_browser('url')
        _loginBusiness = LoginBusiness(driver=self.driver)
        _loginBusiness.login()
        print("Login Success")
        '''
        _aiBusiness = AiBusiness(driver=self.driver)
        print("Create AI")
        deployment_status = _aiBusiness.create_ai()
        self.assertEqual('Deployment succeeded', deployment_status.text, 'Create AI successfully')
        print("Delete AI")
        delete_status = _aiBusiness.delete_ai()
        self.assertEqual('Delete Application Insights resource', delete_status.text, 'Delete AI successfully')
        '''

if __name__ == '__main__':
    unittest.main()

