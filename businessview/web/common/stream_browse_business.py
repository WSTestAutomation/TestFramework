# coding=utf-8
# @Time    :
# @Author  :
# @File    : stream_browse_business.py

from baseview.web.business_web import BusinessWebPage
from page.web.business.common.browse_page import BrowsePage as Page
from common.browser_engine import Logger
import time

class Stream_browse_business(BusinessWebPage):
    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    # TODO
    # def search_for_text(self):

    # TODO
    # def search_for_button(self):

    # TODO
    # def sort_by(self):

    def wait_for_videos_be_loaded(self):
        element = self.find_element(*self._page.items_list_container)
        return element is not None

    def click_show_more_button(self):
        self.click(self._page.show_more)

    def click_video_to_watch_by_index(self, videoIndex=0):
        items = self.driver.find_elements_by_xpath(self._page.items_list[1])
        if len(items) >= videoIndex:
            items[videoIndex].click()
            return True
        else:
            Logger.info('下标超出已加载视频下标。请点击“show more”按钮以加载更多视频。')
            return False
