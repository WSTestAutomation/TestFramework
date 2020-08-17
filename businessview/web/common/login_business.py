# coding=utf-8

from baseview.web.base_web import BaseWebPage
from page.web.login_page import LoginPage as Page
from utilstest.base_yaml import Yaml
import time
import pyautogui
import logging


class LoginBusiness(BaseWebPage):

    data = Yaml(Yaml.web_config_path).read()
    username = data['username']
    password = data['password']

    def __init__(self, driver):
        BaseWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def login(self, user_name=username, password=password):
        self.send_keys(self._page.user_name_input, user_name)
