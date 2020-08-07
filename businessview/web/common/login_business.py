# coding=utf-8

from baseview.web.base_web import BaseWebPage
from page.web.login_page import LoginPage as Page
from utilstest.base_yaml import Yaml


class LoginBusiness(BaseWebPage):

    data = Yaml(Yaml.web_config_path).read()
    username = data['username']
    password = data['password']

    def __init__(self, driver):
        BaseWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def login(self, user_name=username, password=password):
        self.send_keys(self._page.user_name_input, user_name)
        self.click(self._page.next_button)
        self.find_element_click(self._page.click_signin_button, 'Sign in with a username and password instead')
        self.send_keys(self._page.password_input, password)
        self.find_element_click(self._page.sign_button, 'Sign in')
        self.find_element_click(self._page.click_verify_button, 'Sign in with your phone or token device')
        self.click(self._page.yes_button)





