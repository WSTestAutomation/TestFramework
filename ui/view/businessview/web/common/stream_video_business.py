# coding=utf-8
# @Time    :
# @Author  :
# @File    : stream_video_business.py

from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.common.video_page import VideoPage as Page
from ui.lib.browser_engine import Logger

class Stream_video_business(BusinessWebPage):
    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def get_video_statistics_like_number(self):
        return int(self.find_element(*self._page.video_statistics_like).text)

    def click_like_button(self):
        self.click(self._page.like_button)

    def is_liked(self):
        element = self.find_element(*self._page.like_button)
        return element.get_attribute("aria-label") == "Unlike"
