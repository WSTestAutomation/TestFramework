# coding=utf-8

from baseview.web.business_web import BusinessWebPage
from page.web.business.common.login_page import LoginPage as Page
from utilstest.base_yaml import Yaml
from common.browser_engine import Logger
from common.browser_engine import open_browser

data = Yaml(Yaml.web_config_path).read()
env = data['env']
browser = data['browser']
username = data['user']['test1']
password = data['pwd']['commonpwd']

class LoginBusiness(BusinessWebPage):

    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def login(self, user=username, pwd=password):
        is_sucess = False
        if not self.driver.title.startswith('Sign in to your account'):
            # If there's a critial failure and we cannot go ahead, use Logger.excetpion()
            Logger.exception('Not in the LoginPage.')

        try:
            self.send_keys(self._page.user_name_input, user)
            self.click(self._page.next_input)
            # TODO: there is a popup window here and possible we need to input credentials in a differet way...

            self.send_keys(self._page.password_input, pwd)
            self.click(self._page.signin_input)
            if self.driver.current_url.startswith('https://login.windows-ppe.net/common/login'):
                self.click(self._page.no_button)

            # Now it should be in Homepage!
            if user in self.driver.page_source:
                Logger.info('%s is signed in.', user)
                is_sucess = True
            else:
                Logger.error('Sign in failed')
        except Exception as e:
            Logger.error('Exception: %s', format(e))
        finally:
            return is_sucess


def simple_login():
    Logger.info("Login to %s", env)
    driver = open_browser(env, browser)
    login_business = LoginBusiness(driver)
    is_login = login_business.login(user=username, pwd=password)
    if is_login:
        return driver
    return None
