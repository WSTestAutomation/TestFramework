# coding=utf-8
# @Time    :
# @Author  :
# @File    :

import os
import time
import sys
import unittest
from common.appium_desired import appium_android_desired, appium_ios_desired

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from BeautifulReport.BeautifulReport import BeautifulReport
from utilstest.base_runner import BaseAppTestCase


class app_test(BaseAppTestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = appium_android_desired("android_baidumap")

    @BeautifulReport.add_test_img('app_test_test_1{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_1_search_location(self):
        # TODO: 添加测试步骤及断言
        #baidumap = Demo_BaiduMap(self.driver)
        pass


if __name__ == '__main__':
    unittest.main()
