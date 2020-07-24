# coding=utf-8

from utils.read_yaml import YamlReader
import paramiko
import os
'''连接SSH，调用jenkins执行APP业务 调用完后面添加等待时间'''


def ssh_bat_cmd(command):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    yaml_file = os.path.join(base_dir, 'config', 'config.yaml')
    ip = YamlReader(yaml_file).get('ssh').get('ip')
    user = YamlReader(yaml_file).get('ssh').get('user')
    password = YamlReader(yaml_file).get('ssh').get('password')
    port = YamlReader(yaml_file).get('ssh').get('port')
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
    ssh_bat_cmd(command='')