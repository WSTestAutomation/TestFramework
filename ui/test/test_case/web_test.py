# coding=utf-8

import sys
import os
import time
import unittest
from ui.view.businessview.web.common.login_business import simple_login
from common.package.BeautifulReport.BeautifulReport import BeautifulReport
from ui.lib.base_runner import BaseWebTestCase
from common.lib.base_yaml import Yaml
from ui.lib.browser_engine import Logger, web_config_path

class web_test(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)

    # 有异常发生时会自动截图并呈现在报告中，
    # 其他需要呈现在报告里的截图，必须手动添加截图名称。
    @BeautifulReport.add_test_img('web_test-test_1-screenshot1')
    def test_1(self):
        self._testMethodDoc = "Validate topbar navigation"
        # 如果类内的其它test case也需要用到driver，那么需要将self.driver的赋值放到setUpClass()内部
        driver = simple_login()
        self.assertIsNotNone(driver, "成功获取driver！")
        self.driver = driver
        # TODO: add test steps and asserts.
        # 如果没有报错也需要截图，可以调用self.save_img() 方法
        self.save_img('web_test-test_1-screenshot1')
        print('这句话会显示在report中，注意report中截图总是先显示在最下面，而不是呈现在这句话上面')
        #self.driver.close()
        #self.driver.quit()
    

if __name__ == '__main__':
    unittest.main()

