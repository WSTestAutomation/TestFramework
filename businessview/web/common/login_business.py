# coding=utf-8

from baseview.web.base_web import BaseWebPage
from page.web.login_page import LoginPage as Page
from utilstest.base_yaml import Yaml
import time
import pyautogui
from common.browser_engine import Logger


class LoginBusiness(BaseWebPage):

    data = Yaml(Yaml.web_config_path).read()
    username = data['user']['personalAccount']
    password = data['pwd']['commonpwd']

    def __init__(self, driver):
        BaseWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def login(self, user_name=username, password=password):
        if  not self.driver.title.startswith('Sign in to your account'):
            raise Exception('Not in the LoginPage.')
        try:
            self.send_keys(self._page.user_name_input, user_name)
            self.click(self._page.next_button)
            # TODO: there is a popup window here and possible we need to input credentials in a differet way...

            self.send_keys(self._page.password_input, password)
            self.click(self._page.signin_input)
            if self.driver.current_url.startswith('https://login.windows-ppe.net/common/login'):
                self.click(self._page.no_button)

            # Now it should be in Homepage!
            if user_name in self.driver.page_source:
                Logger.info('%s is signed in.', user_name)
            else:
                Logger.error('Sign in failed')
        except Exception as e:
            Logger.critical('Exception: %s', format(e))
