# coding=utf-8

import time
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.getcwd())+os.path.sep+".")
sys.path.append(os.getcwd())
from BeautifulReport.BeautifulReport import BeautifulReport
from utilstest.base_runner import BaseWebTestCase
from common.get_interface_text import get_text
import pandas as pd
from utilstest.base_log import Log
logging = Log().get_logger()

class interface_text_to_csv(BaseWebTestCase):
    
    @BeautifulReport.add_test_img('test_new_ai{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_new_ai(self):
        logging.info("Create csv file")
        base_dir = os.path.dirname(os.path.dirname(__file__))
        test_data_path = os.path.join(base_dir, 'test_data')
        input_file = os.path.join(test_data_path, 'test1.csv')
        logging.info("Open URL")

        ele_json = get_text('url')
        data = pd.DataFrame()
        for i in range(len(ele_json)):
            data = data.append(ele_json[i],ignore_index=True)
            logging.info("Get the url%s data Done" % (i+1))

        pd.DataFrame(data).to_csv(input_file)
        logging.info("Success")

if __name__ == '__main__':
    unittest.main()
