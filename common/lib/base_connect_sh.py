# coding=utf-8

import os
import paramiko
from common.lib.base_yaml import Yaml
'''连接SSH，调用jenkins执行APP业务 调用完后面添加等待时间'''


def ssh_bat_cmd(config_file_path, command):
    """config_file_path 需要是一个YAML文件"""
    config = Yaml(config_file_path).read_get('ssh')
    ip = config.get('ip')
    user = config.get('user')
    password = config.get('password')
    port = config.get('port')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, user, password)
    stdin, stdout, stderr = ssh.exec_command(command)
    stdout_info = stdout.readlines()
    err_info = stderr.readlines()
    if err_info:
        print("{} is failed: {}".format(ip, err_info))
    else:
        print("{} is successful: {}".format(ip, stdout_info))
    ssh.close()


if __name__ == '__main__':
    ssh_bat_cmd(config_file_path = '', command = '')
