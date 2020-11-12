# coding=utf-8

import unittest
from common.lib.base_csv import *
from common.lib.base_yaml import *


def input_parameter(data):
    input_data_path = os.path.join(base_dir, 'config/input_parameter.yaml')
    fr = Yaml(input_data_path).read()
    fr['name'] = data['姓名']
    fr['gender'] = data['性别']
    fr['card_id'] = data['证件号码']
    fr['phone_num'] = data['手机号']
    fr['project_code'] = data['项目代码']
    fr['education'] = data['学历']
    fr['pay'] = data['工资']
    Yaml(input_data_path).write(fr)


"""
if __name__ == '__main__':
    csv_data = read_csv_file(input_file)
    for i in range(0, len(csv_data)-1):
        data = csv_data[i]
        input_parameter(data)
"""
