# coding=utf-8

import sys
import os
sys.path.append(os.path.dirname(os.getcwd())+os.path.sep+".")
sys.path.append(os.getcwd())

import time
import unittest
from businessview.web.common.login_business import simple_login
from BeautifulReport.BeautifulReport import BeautifulReport
from utilstest.base_runner import BaseWebTestCase
from utilstest.base_yaml import Yaml
from common.browser_engine import Logger


class web_test(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)

    @BeautifulReport.add_test_img('test_mainpage{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_mainpage(self):
        # 登录，需要改配置文件指定环境、浏览器及登录凭证
        self.driver = simple_login()
        time.sleep(1)
        # 添加步骤及断言
        # self.assertTrue()


if __name__ == '__main__':
    unittest.main()
