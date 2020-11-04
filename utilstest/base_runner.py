# coding=utf-8

import os
import unittest
import warnings
import logging
from utilstest.base_log import Log
base_dir = os.path.dirname(os.path.dirname(__file__))


class BaseAppTestCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.switch_to.default_content()
            cls.driver.close()
            cls.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def save_img(self, img_name):
        img_path = os.path.join(base_dir, 'img')
        if self.driver is not None:
            self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))


class BaseWebTestCase(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)
        warnings.simplefilter("ignore", DeprecationWarning)

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            cls.driver.switch_to.default_content()
            cls.driver.close()
            cls.driver.quit()

    def setUp(self):
        logging.info("-----Test Start-----")

    def tearDown(self):
        logging.info("-----Test End-----")

    def save_img(self, img_name):
        img_path = os.path.join(base_dir, 'img')
        if self.driver is not None:
            self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))
