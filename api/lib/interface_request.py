# coding=utf-8

import urllib.request
import json
import os
import sys
import requests
import xlrd

base_dir = os.path.dirname(os.path.dirname(__file__))

def get_text(num, api_name, api_host, request_url, method, request_data_type, request_data, check_point):
    # 构造请求headers
    headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With' : 'XMLHttpRequest',
                    'Connection' : 'keep-alive',
                    'Referer' : 'http://' + api_host,
                    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
                }
    # 判断请求方式，如果是GET，则调用get请求，POST调post请求，都不是，则抛出异常
    if method == "GET":
        r = requests.get(url=api_host+request_url, params=json.loads(request_data), headers=headers)
        # 获取请求状态码
        status = r.status_code
        print(status)
        # 获取返回值
        resp = r.text
        if status == 200:
            # 断言，判断设置的断言值，是否在返回值里面
            if check_point in str(r.text):
                print("第{}条用例'{}'执行成功，状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
                return status, resp
            else:
                print("第{}条用例'{}'执行失败！！！状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
                return status, resp
        else:
            print("第{}条用例'{}'执行失败！！！状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
            return status, resp
    elif method == "POST":
        # 跟GET里面差不多，就不一一注释了
        r = requests.post(url=api_host+request_url, params=json.loads(request_data), headers=headers)
        status = r.status_code
        resp = r.text
        if status == 200:
            if check_point in str(r.text):
                print("第{}条用例'{}'执行成功，状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
                return status, resp
            else:
                print("第{}条用例'{}'执行失败！！！状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
                return status, resp
        else:
            print("第{}条用例'{}'执行失败！！！状态码为{}，结果返回值为{}.".format(num, api_name, status, r.text))
            return status, resp
    else:
        print("第{}条用例'{}'请求方式有误！！！请确认字段【Method】值是否正确，正确值为大写的GET或POST。".format(num, api_name))
        return 400, "请求方式有误"


# if __name__ == "__main__":
#     erroe_case = interface_test(num, api_name, api_host, request_url, method, request_data_type, request_data, check_point)

