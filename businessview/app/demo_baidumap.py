# coding=utf-8

from baseview.app.base_app import BaseAppPage
from page.app.base_page import BasePage as Page
from page.app.demo_baidumap import BaiduMapPage


class Demo_BaiduMap(BaseAppPage):
    def __init__(self, driver):
        BaseAppPage.__init__(self=self, driver=driver)
        self._page = Page()

    def search_location(self, location_name):
        route_btn = self.find_element(BaiduMapPage.route_btn)
        route_btn.click()
        
        dest_tv = self.find_element(BaiduMapPage.dest_tv)
        dest_tv.click()
        
        dest_input = self.find_element(BaiduMapPage.dest_input)
        dest_input.send_keys(location_name)
        
        search_btn = self.find_element(BaiduMapPage.search_btn)
        search_btn.click()

        # TODO: 获取搜索结果
        res = {}
        return res
