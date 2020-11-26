# coding=utf-8

from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.common.login_page import LoginPage as Page
from ui.lib.browser_engine import Logger, web_config, open_browser

ENV = web_config['env']
BROWSER = web_config['browser']
USERNAME = web_config['user']['test1']
PASSWORD = web_config['pwd']['commonpwd']

class LoginBusiness(BusinessWebPage):

    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def login(self, user, pwd):
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
            if user.lower() in self.driver.page_source.lower():
                Logger.info('%s is signed in.', user)
                is_sucess = True
            else:
                Logger.error('Sign in failed')
        except Exception as e:
            Logger.error('Exception: %s', format(e))
        finally:
            return is_sucess


def simple_login():
    Logger.info("Login to %s", ENV)
    driver = open_browser(ENV, BROWSER)
    login_business = LoginBusiness(driver)
    is_login = login_business.login(user=USERNAME, pwd=PASSWORD)
    if is_login:
        return driver
    return None
