# coding=utf-8
# @Time    :
# @Author  :
# @File    :

import os
import time
import sys
import unittest

from businessview.app.common.common_fun import Common

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from BeautifulReport.BeautifulReport import BeautifulReport
from utilstest.base_runner import BaseAppTestCase


class TestScenario1(BaseAppTestCase):
    @classmethod
    def setUpClass(cls, env):
        super(TestScenario1, cls).setUpClass(env="ios")

    @BeautifulReport.add_test_img('test_app_{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_app(self):
        print("1. select log in system.")
        common = Common(self.driver)
        common.select_env_and_confirm(3)


if __name__ == '__main__':
    unittest.main()
