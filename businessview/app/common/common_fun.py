# coding=utf-8

from baseview.app.base_app import BaseAppPage
from page.app.base_page import BasePage as Page


class Common(BaseAppPage):
    def __init__(self, driver):
        BaseAppPage.__init__(self=self, driver=driver)
        self._page = Page()

    def select_env_and_confirm(self, index):
        self.send_keys(self._page.select_env_text, index)
        self.click(self._page.confirm_btn)
