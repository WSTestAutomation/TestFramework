# coding=utf-8

import sys
import os
import time
import unittest
from ui.view.businessview.web.common.login_business import simple_login
from ui.view.businessview.web.common.stream_topbar_business import *
from ui.view.businessview.web.common.stream_browse_business import *
from ui.view.businessview.web.common.stream_video_business import *
from ui.lib.base_runner import BaseWebTestCase
from common.lib.base_yaml import Yaml
from ui.lib.browser_engine import Logger, web_config_path


class web_test(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)
        self.data = Yaml(web_config_path).read()
        self.env = self.data['env']
        self.homeUrl = self.data['portal'][self.env].rstrip("/")

    def test_mainpage(self):
        self.driver = simple_login()
        stream_topbar_business = Stream_topbar_business(self.driver)
        stream_browse_business = Stream_browse_business(self.driver)
        stream_video_business = Stream_video_business(self.driver)

        # dicover video link
        stream_topbar_business.click_topbar_button_discover()
        stream_topbar_business.click_topbar_link(stream_topbar_business.discover_dropdown_menu_dict['Videos'])

        # in browse page
        stream_browse_business.wait_for_videos_be_loaded()
        stream_browse_business.click_video_to_watch_by_index(0)
        self.assertTrue('/video/' in self.driver.current_url.rstrip("/"), '正在浏览视频页')
                
        # in video page
        if stream_video_business.is_liked():
            stream_video_business.click_like_button()
        like_count = stream_video_business.get_video_statistics_like_number()
        Logger.info("当前喜欢人数：%s", like_count)
        time.sleep(3)

        stream_video_business.click_like_button()
        like_count2 = stream_video_business.get_video_statistics_like_number()
        Logger.info("当前喜欢人数：%s", like_count2)
        self.assertTrue((like_count+1) == like_count2, '喜欢数成功+1')
        time.sleep(3)

        stream_video_business.click_like_button()
        like_count3 = stream_video_business.get_video_statistics_like_number()
        Logger.info("当前喜欢人数：%s", like_count3)
        self.assertTrue(like_count == like_count3, '喜欢数成功-1')

if __name__ == '__main__':
    unittest.main()
