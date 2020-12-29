# coding=utf-8

import unittest
from common.lib.base_yaml import Yaml
from ui.view.businessview.web.common.login_business import simple_login
from common.package.BeautifulReport.BeautifulReport import BeautifulReport
from ui.lib.base_runner import BaseWebTestCase
from ui.lib.browser_engine import Logger, web_config_path
from ui.view.businessview.web.admin.navigation_business import *

class Admin_navigation(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)

    @classmethod
    def setUpClass(cls):
        super(Admin_navigation, cls).setUpClass()
        cls.data = Yaml(web_config_path).read()
        cls.env = cls.data['env']
        cls.user = cls.data['user']['tenantadmin']
        cls.driver = simple_login(username=cls.user)
        cls.navigation_business = None

    def test_admin_navigation_1(self):
        """
        验证登录
        """
        url = self.data['portal'][self.env] + '/admin'
        self.driver.get(url)
        self.navigation_business = Navigation_business(self.driver)
        self.assertTrue(self.navigation_business.is_sign_in_successully(), '页面正常展示')

    @BeautifulReport.depend_on("test_admin_navigation_1")
    @BeautifulReport.add_test_img('admin_navigation-test_2')
    def test_admin_navigation_2(self):
        """
        验证：
        1. 无法点击的只检查text内容，或跳过
        2. 可以点击且可以展开的，需要检验 展开/闭合的功能
        3. 可以点击且右侧有内容的需要检验右侧
        """
        self.navigation_business = Navigation_business(self.driver)
        
        ## 循环
        for name, item in self.navigation_business.menu.items():
            with self.subTest(name=name):
                # 验证1
                if item.is_clickable is False:
                    pass

                # 验证2
                # 假如可以展开/收起则测，否则跳过
                if item.has_subitems:
                    self.assertTrue(item.expand(), "确认'"+name+"'展开子项目的功能")
                    self.assertTrue(item.contract(), "确认'"+name+"'收起子项目的功能")
                #navigation_business.menu['Spotlight videos'].click()
                # 验证3
                self.validate_tab_page(self.navigation_business.menu, name)


    def validate_tab_page(self, dict_menu, item_name):
        item: Navigation_business.Admin_settings_menu_item = dict_menu[item_name]
        if item.tab_by is None:
            return
        if item.parent is not None:
            # 确保当前父节点已展开
            parent = dict_menu[item.parent]
            is_parent_expanded = parent.expand()
            # 点击并确认右侧内容
            if is_parent_expanded:
                item.click()
            # 元素存在， 且为父节点下唯一子元素
            ele_tab_page = item.obj.find_element(*item.tab_by)
            self.assertIsNotNone(ele_tab_page, ('页面'+ item.name + '已显示'))
            elements = self.navigation_business.get_elements_under_tab_page()
            self.assertEqual(len(elements), 1, "其他功能页面不显示")


if __name__ == '__main__':
    unittest.main()
