# coding=utf-8
# @Time    :
# @Author  :
# @File    : stream_topbar_business.py

from enum import Enum
from baseview.web.business_web import BusinessWebPage
from page.web.business.common.topbar_page import TopbarPage as Page
from common.browser_engine import Logger

class Stream_topbar_business(BusinessWebPage):
    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()
        self.discover_button_element = None
        self.discover_dropmenu_element = None
        self.discover_dropdown_menu_dict = {'video':    self._page.discover_video_link,
                                            'channel':  self._page.discover_channel_link,
                                            'people':   self._page.discover_people_link,
                                            'group':    self._page.discover_group_link
                                            }

    def click_topbar_button(self, fname):
        if self.is_element_clickable(fname):
            self.click(fname)
        else:
            element = self.find_element(*fname)
            self.perform_javascript_click(element)

    def click_topbar_link(self, lname):
        if self.is_element_clickable(lname):
            self.click(lname)
        else:
            element = self.find_element(*lname)
            self.perform_javascript_click(element)

    def click_topbar_button_home(self):
        self.click_topbar_button(self._page.home_link)

    def click_topbar_button_discover(self):
        if self.discover_button_element is None:
            self.discover_button_element = self.find_element(*self._page.discover_button)
        if self.discover_dropmenu_element is None:
            self.discover_dropmenu_element = self.find_element(*self._page.discover_dropdown_menu)
        self.click_topbar_button(self._page.discover_button)
