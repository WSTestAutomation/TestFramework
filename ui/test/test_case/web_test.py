# coding=utf-8

import sys
import os
import time
import unittest
from ui.view.businessview.web.common.login_business import simple_login
from common.package.BeautifulReport.BeautifulReport import BeautifulReport
from ui.view.businessview.web.common.stream_topbar_business import *
from ui.lib.base_runner import BaseWebTestCase
from common.lib.base_yaml import Yaml
from ui.lib.browser_engine import Logger, web_config_path

class web_test(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
        #self.data = Yaml(web_config_path).read()
        #self.env = self.data['env']

    # 有异常发生时会自动截图并呈现在报告中，
    # 其他需要呈现在报告里的截图，必须手动添加截图名称。
    @BeautifulReport.add_test_img('web_test-test_1-screenshot1')
    def test_topbar_navigation(self):
        self._testMethodDoc = "Validate topbar navigation"
        self.driver = simple_login()
        stream_topbar_business = Stream_topbar_business(self.driver)
        # TODO: add test steps and asserts.
        # 如果没有报错也需要截图，可以调用self.save_img() 方法
        self.save_img('web_test-test_1-screenshot1')
        # stream_topbar_business.goto_feature_page(FeaturePage.mycontent_videos)
        # self.assertTrue(self.driver.current_url.endswith('/studio/videos'))
        # stream_topbar_business.goto_feature_page(FeaturePage.mycontent_channels)
        # self.assertTrue(self.driver.current_url.endswith('/studio/channels'))

if __name__ == '__main__':
    unittest.main()

