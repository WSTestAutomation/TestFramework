# coding=utf-8
# @Time :
# @Author :
# @File : base_appium_server.py

import os
import threading
import logging
import platform
import subprocess
import random
from multiprocessing import Process
from ui.lib.base_device import get_device_udid


class RunServer(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)


class AppiumServer:
    def __init__(self, kwargs=None):
        self.kwargs = kwargs

    def start_server(self):
        """ start appium server"""
        cmd = "appium --session-override  -p %s -bp %s -U %s" % (
            self.kwargs["port"], self.kwargs["bport"], self.kwargs["udid"]
        )
        logging.info("run appium cmd: %s" % cmd)
        if platform.system() == "Windows":  # windows下启动server
            t1 = RunServer(cmd)
            p = Process(target=t1.start())
            p.start()
            while True:
                print("--------start_win_server-------------")
                if p.run("http://127.0.0.1:" + self.kwargs["port"] + "/wd/hub" + "/status"):
                    print("-------win_server_ 成功--------------")
                    break
        else:
            appium = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
            while True:
                appium_line = appium.stdout.readline().strip().decode()
                if 'listener started' in appium_line or 'Error: listen' in appium_line:
                    logging.info("Appium server start ")
                    break

    def stop_server(self):
        if platform.system() == 'Windows':
            os.popen("taskkill /f /im node.exe")
        else:
            # mac
            cmd = "lsof -i :{0}".format(self.kwargs["port"])
            cmd_info = os.popen(cmd).readlines()
            cmd_lists = cmd_info[1].split("    ")
            cmd_list = cmd_lists[1].split(" ")
            os.popen("kill -9 {0}".format(cmd_list[0]))
            logging.info("Kill server success.")


if __name__ == '__main__':
    app = {
        'udid': get_device_udid(),
        "port": str(random.randint(4700, 4900)),
        "bport": str(random.randint(4700, 4900)),
        "systemPort": str(random.randint(4700, 4900))
    }
    print(app)
    appium_server = AppiumServer(app)
    appium_server.start_server()
    appium_server.stop_server()
