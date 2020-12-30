# coding=utf-8
# @Author  : Qian Liu

import unittest
from common.package.BeautifulReport.BeautifulReport import BeautifulReport
from ui.view.businessview.web.common.login_business import simple_login
from ui.view.businessview.web.admin.manage_deleted_users_business import *
from ui.lib.base_runner import BaseWebTestCase
from common.lib.base_yaml import Yaml
from ui.lib.browser_engine import Logger, web_config_path


class web_test_manage_delete_user(BaseWebTestCase):
    def __init__(self, *args, **kwargs):
        BaseWebTestCase.__init__(self, *args, **kwargs)

    @classmethod
    def setUpClass(cls):
        super(web_test_manage_delete_user, cls).setUpClass()
        cls.data = Yaml(web_config_path).read()
        cls.env = cls.data['env']
        cls.user = cls.data['user']['tenantadmin']
        cls.driver = simple_login(username=cls.user)
        url = cls.data['portal'][cls.env] + '/admin'
        cls.driver.get(url)

    # 验证：通过关键字搜索用户是否存在
    def test_admin_manage_delete_user_01(self):
        """
        搜索不存在的用户
        """
        manage_deleted_users = Manage_deleted_users_business(self.driver)        
        manage_deleted_users.search_deleted_users("user_not_exist")
        user_exist = manage_deleted_users.get_search_input_exist_user()
        self.assertFalse(user_exist, "关键字搜索用户不存在！")
        #TODO: 检验界面信息


    # 验证：通过关键字搜索用户是否存在
    def test_admin_manage_delete_user_02(self):
        """
        搜索存在的用户
        """
        manage_deleted_users = Manage_deleted_users_business(self.driver)
        manage_deleted_users.search_deleted_users("test")
        user_exist = manage_deleted_users.get_search_input_exist_user()
        self.assertTrue(user_exist, "关键字搜索用户存在！")
            
    # 验证edit按钮能否点击
    def test_admin_manage_delete_user_03(self):
        """
        验证Edit按钮
        """
        manage_deleted_users = Manage_deleted_users_business(self.driver)
        manage_deleted_users.click_edit_button()
        self.assertEqual("#icon_edit", manage_deleted_users.get_edit_button(), "成功点击edit按钮！")

    # 验证edit user details中cancel按钮能否点击
    @BeautifulReport.depend_on('test_admin_manage_delete_user_03')
    def test_admin_manage_delete_user_04(self):
        """
        验证Cancel按钮
        """
        manage_deleted_users = Manage_deleted_users_business(self.driver)
        self.assertTrue(manage_deleted_users.get_cancel_edit_button(), "cancel按钮可点击！")
        manage_deleted_users.cancel_edit_button()
        self.assertEqual("Manage deleted users", manage_deleted_users.get_manage_deleted_users_model(), "点击成功")

    # 验证edit user details中save按钮能否点击
    def test_admin_manage_delete_user_05(self):
        """
        验证Save按钮
        """
        manage_deleted_users = Manage_deleted_users_business(self.driver)
        manage_deleted_users.edit_user_name("test_user")
        self.assertTrue(manage_deleted_users.get_save_button(), "save按钮可点击！")
        manage_deleted_users.click_save_button()
        self.assertEqual("Manage deleted users", manage_deleted_users.get_manage_deleted_users_model(), "点击成功")
        # TODO: 需要确认Name真的被更改了，比较Edit前后的变化

    # 验证delete按钮
    def test_admin_manage_delete_user_06(self):
        """
        验证Delete按钮
        """
        manage_deleted_users = Manage_deleted_users_business(self.driver)
        manage_deleted_users.click_delete_button()
        self.assertEqual("#icon_delete", manage_deleted_users.get_delete_button(), "成功点击delete按钮！")

    # 验证cancel按钮
    @BeautifulReport.depend_on('test_admin_manage_delete_user_06')
    def test_admin_manage_delete_user_07(self):
        """
        验证Delete过程中的Cancel按钮
        """
        manage_deleted_users = Manage_deleted_users_business(self.driver)
        self.assertTrue(manage_deleted_users.get_cancel_delete_button())
        manage_deleted_users.cancel_delete_button()
        self.assertEqual("Manage deleted users", manage_deleted_users.get_manage_deleted_users_model(), "点击成功")
        #TODO: 需要判断对话框消失


if __name__ == "__main__":
    unittest.main()