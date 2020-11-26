# coding=utf-8

import os
import unittest
import time
from common.package.BeautifulReport.BeautifulReport import BeautifulReport
from common.lib.base_config import UI_OUTPUT_DIR, UI_TEST_DIR
#from common.lib.base_mail_smtp import Email
from common.lib.base_mail import email

test_cases_path = os.path.join(UI_TEST_DIR, 'test_case')
report_path = os.path.join(UI_OUTPUT_DIR, 'report')

# 如果是web 测试，需确定drivers下游对应浏览器的webdriver
# 如果是app 测试，先确定appium服务已经开启，并确保端口设置正确
test_suite1 = unittest.TestLoader().discover(test_cases_path, pattern='web_test.py')

suite = unittest.TestSuite(test_suite1)
result = BeautifulReport(suite)
report_file = "autotest_report_" + time.strftime('%Y%m%d%H%M%S') + ".html"

result.report(filename=report_file,
              description='UI Automation Report', log_path=report_path)

#report_file_path = os.path.join(report_path, report_file)
#Email(path=report_file_path).send()
email(report_path, report_file)
