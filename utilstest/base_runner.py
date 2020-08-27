# coding=utf-8

import os
import unittest
import warnings
from businessview.app.common.common_fun import Common
from common.appium_desired import appium_android_desired, appium_desired
from utilstest.base_log import Log
base_dir = os.path.dirname(os.path.dirname(__file__))


class BaseAppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls, env):
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)

        if env == 'None':
            cls.driver = None
        elif env =='ios':
            cls.driver = appium_desired('app_path', 4723)
            cls.common = Common(cls.driver)
            # cls.common.select_env_and_confirm(5)
        elif env =='android':
            cls.driver = appium_android_desired()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def save_img(self, img_name):
        img_path = os.path.join(base_dir, 'img')
        if self.driver is not None:
            self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))


class BaseWebTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.driver = None

    def tearDown(self):
        if self.driver is not None:
            self.driver.switch_to.default_content()
            self.driver.close()
            self.driver.quit()

    def save_img(self, img_name):
        img_path = os.path.join(base_dir, 'img')
        if self.driver is not None:
            self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))