# coding=utf-8
# @Time    :
# @Author  :
# @File    : stream_topbar_business.py

from enum import Enum
from baseview.web.business_web import BusinessWebPage
from page.web.business.common.topbar_page import TopbarPage as Page
from common.browser_engine import Logger

class FeaturePage(Enum):
    home = 0
    discover = 10
    discover_videos = 11
    discover_channels = 12
    discover_people = 13
    discover_groups = 14
    mycontent = 20
    mycontent_videos = 21
    mycontent_groups = 22
    mycontent_channels = 23
    mycontent_meetings = 24
    mycontent_watchlist = 25
    mycontent_followed_channels = 26
    mycontent_recycle_bin = 27
    create = 30
    create_video = 31
    create_live = 32
    create_group = 33
    create_channel = 34
    create_screen_recording = 35

feature_locator = {
    FeaturePage.home.value : Page.home_link,
    FeaturePage.discover.value : Page.discover_button,
    FeaturePage.discover_videos.value : Page.discover_video_link,
    FeaturePage.discover_channels.value : Page.discover_channel_link,
    FeaturePage.discover_groups.value : Page.discover_group_link,
    FeaturePage.mycontent.value : Page.myContent_button,
    FeaturePage.mycontent_videos.value : Page.myContent_videos_link,
    FeaturePage.mycontent_channels.value : Page.myContent_channels_link,
    FeaturePage.create.value : Page.create_button,
    FeaturePage.create_video.value : Page.create_upload_link,
}

class Stream_topbar_business(BusinessWebPage):

    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()


    def goto_feature_page(self, feature: FeaturePage):
        # 先点击下拉框
        button = feature_locator[feature.value // 10 * 10]
        self.click(button)
        
        # 再点击具体功能
        if (feature.value % 10 != 0):
            link = feature_locator[feature.value]
            self.click(link)

    def goto_homepage(self):        
        self.goto_feature_page(FeaturePage.home)        
        # TODO
        # Ensure it is home page!!!
