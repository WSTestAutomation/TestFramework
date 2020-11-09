# coding=utf-8

import os
import unittest
import warnings
import logging
from common.lib.base_config import UI_OUTPUT_DIR


class BaseAppTestCase(unittest.TestCase):
    driver = None
    output_dir = UI_OUTPUT_DIR
    screenshot_dir = os.path.join(UI_OUTPUT_DIR, 'img')

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
        img_path = os.path.join(UI_OUTPUT_DIR, 'img')
        if self.driver is not None:
            self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))


class BaseWebTestCase(unittest.TestCase):
    driver = None
    output_dir = UI_OUTPUT_DIR
    screenshot_dir = os.path.join(UI_OUTPUT_DIR, 'img')

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
        img_path = os.path.join(UI_OUTPUT_DIR, 'img')
        if self.driver is not None:
            self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))
