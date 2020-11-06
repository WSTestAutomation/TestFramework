# coding=utf-8

import sys
import os
sys.path.append(os.path.dirname(os.getcwd())+os.path.sep+".")
sys.path.append(os.getcwd())
import unittest
import time
from BeautifulReport import BeautifulReport
from utilstest.base_mail_smtp import Email

base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
test_cases_path = os.path.join(base_dir, 'test_case')
report_path = os.path.join(base_dir, 'report')

# 如果是web 测试，需确定drivers下游对应浏览器的webdriver
# 如果是app 测试，先确定appium服务已经开启，并确保端口设置正确
test_suite1 = unittest.TestLoader().discover(test_cases_path, pattern='web_test.py')

suite = unittest.TestSuite(test_suite1)
result = BeautifulReport(suite)
report_file = "autotest_report_" + time.strftime('%Y%m%d%H%M%S') + ".html"

result.report(filename=report_file,
              description='UI Automation Report', log_path=report_path)

report_file_path = os.path.join(report_path, report_file)
# Email(receiver='', path=report_file_path).send()
