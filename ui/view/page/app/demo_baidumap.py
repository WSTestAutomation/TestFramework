# coding=utf-8

from appium.webdriver.common.mobileby import MobileBy


class BaiduMapPage:
    route_btn = (MobileBy.ID, 'com.baidu.BaiduMap:id/home_route_btn')
    dest_tv = (MobileBy.ID, 'com.baidu.BaiduMap:id/route_search_input_end_text')
    dest_input = (MobileBy.ID, 'com.baidu.BaiduMap:id/edittext_searchbox_search_input')
    search_btn = (MobileBy.ID, 'com.baidu.BaiduMap:id/tv_searchbox_history_search')
