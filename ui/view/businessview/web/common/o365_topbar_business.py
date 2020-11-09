# coding=utf-8
# @Time    :
# @Author  :
# @File    : o365_topbar_business.py

from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.common.topbar_page import TopbarPage as Page
from ui.lib.browser_engine import Logger

class O365_topbar_business(BusinessWebPage):
    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def open_settings_panel(self):
        # TODO
        pass
