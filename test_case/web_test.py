# coding=utf-8

import sys
import os
sys.path.append(os.path.dirname(os.getcwd())+os.path.sep+".")
sys.path.append(os.getcwd())

import time
import unittest
from businessview.web.common.login_business import simple_login
from businessview.web.common.stream_topbar_business import *
from utilstest.base_runner import BaseWebTestCase
from utilstest.base_yaml import Yaml
from common.browser_engine import Logger


class web_test(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
        #self.data = Yaml(Yaml.web_config_path).read()
        #self.env = self.data['env']

    def test_mainpage(self):
        self.driver = simple_login()
        stream_topbar_business = Stream_topbar_business(self.driver)
        stream_topbar_business.goto_feature_page(FeaturePage.discover_videos)
        stream_topbar_business.goto_feature_page(FeaturePage.mycontent_channels)
        stream_topbar_business.goto_feature_page(FeaturePage.create_group)
        stream_topbar_business.goto_homepage()


if __name__ == '__main__':
    unittest.main()

