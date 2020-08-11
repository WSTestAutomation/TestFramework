#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import unittest
import requests
import xlrd
import time
import sys
sys.path.append(os.path.dirname(os.getcwd())+os.path.sep+".")
sys.path.append(os.getcwd())
from utilstest.base_runner import BaseWebTestCase
from BeautifulReport.BeautifulReport import BeautifulReport
from common.interface_request import get_text


base_dir = os.path.dirname(os.path.dirname(__file__))

class interface_test(BaseWebTestCase):
    
    @BeautifulReport.add_test_img('test_new_ai{}'.format(time.strftime('%Y%m%d%H%M%S')))
    def test_new_ai(self):
        test_data_path = os.path.join(base_dir, 'test_data')
        test_case_file = os.path.join(test_data_path, "testcases.xlsx")
        if not os.path.exists(test_case_file):
            print("测试用例excel文件存在或路径有误！")
            sys.exit()

        test_case = xlrd.open_workbook(test_case_file)
        # 获取第一个sheet，下标从0开始
        table = test_case.sheet_by_index(0)
        # 记录错误用例
        error_cases = []
        # 一张表格读取下来，其实就像个二维数组，无非是读取第一行的第几列的值，由于下标是从0开始，第一行是标题，所以从第二行开始读取数据
        for i in range(1, table.nrows):
            num = str(int(table.cell(i, 0).value)).replace("\n", "").replace("\r", "")
            api_name = table.cell(i, 1).value.replace("\n", "").replace("\r", "")
            api_host = table.cell(i, 2).value.replace("\n", "").replace("\r", "")
            request_url = table.cell(i, 3).value.replace("\n", "").replace("\r", "")
            method = table.cell(i, 4).value.replace("\n", "").replace("\r", "")
            request_data_type = table.cell(i, 5).value.replace("\n", "").replace("\r", "")
            request_data = table.cell(i, 6).value.replace("\n", "").replace("\r", "")
            check_point = table.cell(i, 7).value.replace("\n", "").replace("\r", "")
            print(num, api_name, api_host, request_url, method, request_data_type, request_data, check_point)
            try:
                status, resp = get_text(num, api_name, api_host, request_url, method, 
                                                request_data_type, request_data, check_point)
                if status != 200 or check_point not in resp:
                    # append只接收一个参数，所以要讲四个参数括在一起，当一个参数来传递
                    # 请求失败，则向error_cases中增加一条记录
                    error_cases.append((num + " " + api_name, str(status), api_host + request_url))
            except Exception as e:
                print(e)
                print("第{}个接口请求失败，请检查接口是否异常。".format(num))
                # 访问异常，也向error_cases中增加一条记录
                error_cases.append((num + " " + api_name, "请求失败", api_host + request_url))
        if len(error_cases) > 0:
            html = '<html><body>接口自动化扫描，共有 ' + str(len(error_cases)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th></tr>'
            for test in error_cases:
                html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2] + '</td></tr>'
            with open ("report.html", "w", encoding='UTF-8') as f:
                f.write(html)
        else:
            print("本次测试，所有用例全部通过")

if __name__ == '__main__':
    unittest.main()