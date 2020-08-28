# coding=utf-8

from baseview.web.base_web import BaseWebPage
from page.web.login_page import LoginPage as Page
from utilstest.base_yaml import Yaml
from common.browser_engine import Logger


class LoginBusiness(BaseWebPage):

    data = Yaml(Yaml.web_config_path).read()
    username = data['user']['personalAccount']
    password = data['pwd']['commonpwd']

    def __init__(self, driver):
        BaseWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def login(self, user_name=username, password=password):
        is_sucess = False 
        if not self.driver.title.startswith('Sign in to your account'):
            # If there's a critial failure and we cannot go ahead, use Logger.excetpion()
            Logger.exception('Not in the LoginPage.')

        try:
            self.send_keys(self._page.user_name_input, user_name)
            self.click(self._page.next_input)
            # TODO: there is a popup window here and possible we need to input credentials in a differet way...

            self.send_keys(self._page.password_input, password)
            self.click(self._page.signin_input)
            if self.driver.current_url.startswith('https://login.windows-ppe.net/common/login'):
                self.click(self._page.no_button)

            # Now it should be in Homepage!
            if user_name in self.driver.page_source:
                Logger.info('%s is signed in.', user_name)
                is_sucess = True
            else:
                Logger.error('Sign in failed')
        except Exception as e:
            Logger.error('Exception: %s', format(e))
        finally:
            return is_sucess
