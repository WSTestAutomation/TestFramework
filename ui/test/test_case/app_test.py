# coding=utf-8
# @Time    :
# @Author  :
# @File    :

import time
import unittest
from ui.lib.appium_desired import appium_desired
from ui.view.businessview.app.demo_baidumap import Demo_BaiduMap
from ui.lib.base_runner import BaseAppTestCase
from common.package.BeautifulReport.BeautifulReport import BeautifulReport


class app_test(BaseAppTestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = appium_desired("android_baidumap")

    # 有异常发生时会自动截图并呈现在报告中，
    # 其他需要呈现在报告里的截图，必须手动添加截图名称。
    @BeautifulReport.add_test_img()
    def test_1_search_location(self):
        baidumap = Demo_BaiduMap(self.driver)

        scenarios = {'人民广场': {'结果1':'', '结果2':'', '结果3':''}, '微创软件':{'结果1':'', '结果2':'', '结果3':''}}
        for keyword,exp_results in scenarios.items():
            res = baidumap.search_location(keyword)
            self.assertTrue(len(res) >= len(exp_results), "有足够返回结果")
            for index,location in exp_results.items():
                # TODO: 验证实际结果中包含期望结果
                pass


    @unittest.skip
    @BeautifulReport.add_test_img()
    def test_2_get_road(self):
        pass

if __name__ == '__main__':
    #如果无法连接设备，先确认是否开启了appium server
    unittest.main()
