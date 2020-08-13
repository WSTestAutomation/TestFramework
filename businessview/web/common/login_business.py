# coding=utf-8

from baseview.web.base_web import BaseWebPage
from page.web.login_page import LoginPage as Page
from utilstest.base_yaml import Yaml
import time
import pyautogui


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
        time.sleep(5)
        pyautogui.typewrite(message=user_name)
        pyautogui.press('tab')
        pyautogui.typewrite(message=password)
        pyautogui.press('Enter')
        self.click(self._page.click_verify_button)
        getTotal = self.find_element_by_xpath(self._page.check_login_result)
        try:
            assert getTotal.text == "Learn how to use Microsoft Stream"
            print ('Login Success')
        except Exception as e:
            print ('Assertion test fail.', format(e))




