# coding=utf-8

import sys
import os
sys.path.append(os.path.dirname(os.getcwd())+os.path.sep+".")
sys.path.append(os.getcwd())

import unittest
from businessview.web.common.search_business import SearchBusiness
from baseview.web.base_web import BaseWebPage
from page.web.search_page import SearchPage as Page
from common.browser_engine import Logger

class Search_test(BaseWebPage):
    def __init__(self, driver):
        BaseWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def test_search(self):
        Logger.info('test_search')
        _searchBusiness = SearchBusiness(driver=self.driver)
        _searchBusiness.search_for_videos('test', "Videos", False, firstSearch=True)
        _searchBusiness.search_for_videos('测试', "Videos", False)
        _searchBusiness.search_for_videos('test', "Videos", True)

        # change to channels button
        self.click(self._page.click_channels_button)
        getSearchForText = self.find_elements_by_xpath(self._page.check_search_for_text)
        for i in getTitleText:
            assert "Search for channels" in i.text
        self.search_for_videos('测试', "Channels", False)

        # change to People button
        self.click(self._page.click_People_button)
        getSearchForText = self.find_elements_by_xpath(self._page.check_search_for_text)
        for i in getTitleText:
            assert "Search for people" in i.text
        self.search_for_videos('test', "People", False)

        # My content Vidio
        self.find_element_click(self._page.my_content_column, "My content")
        self.click(self._page.my_content_video)
        self.search_for_videos('test', "Videos", False)
        self.search_for_videos('测试', "Videos", False)
        self.search_for_videos('000', "Videos", False)

        # My content channels
        self.click(self._page.my_content_channels)
        self.search_for_videos('test', "Channels", False, Browser="My content Channels")
        self.search_for_videos('测试', "Channels", False, Browser="My content Channels")
        self.search_for_videos('2222222', "Channels", False, Browser="My content Channels")

        # My content My watchlists
        self.click(self._page.my_content_my_watchlists)
        self.search_for_videos('test', "watchlists", False, Browser="My content My watchlists")
        self.search_for_videos('测试', "watchlists", False, Browser="My content My watchlists")
        self.search_for_videos('2222222', "watchlists", False, Browser="My content My watchlists")

        # My content followed
        self.click(self._page.my_content_my_followed)
        self.search_for_videos('test', "followed", False, Browser="My content folloewd")
        self.search_for_videos('2222222', "followed", False, Browser="My content folloewd")
        self.search_for_videos('测试', "followed", False, Browser="My content folloewd")

        # Video details
        self.find_element_click(self._page.my_content_column, "Discover")
        self.click(self._page.my_content_video)
        self.search_for_videos('测试', "Videos", False)
        
if __name__ == '__main__':
    unittest.main()

