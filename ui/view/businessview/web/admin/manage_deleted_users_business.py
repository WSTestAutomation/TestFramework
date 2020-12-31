# coding=utf-8
# @Author  : Qian Liu
# @File    : manage_deleted_users_business.py

import time
from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.admin.manage_deleted_users_page import ManageDeletedUserPage as Page
from ui.lib.browser_engine import Logger

class Manage_deleted_users_business(BusinessWebPage):
    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def search_deleted_users(self, text):
        self.click(self._page.manage_deleted_users)
        self.send_keys(self._page.search_delete_users, text, need_clear=True, need_enter=True)

    def click_edit_button(self):
        time.sleep(1)
        edit_button = self.find_element(*self._page.edit_button)
        self.action_catena(edit_button, "单击")

    def edit_user_name(self, text):
        self.click_edit_button()
        self.send_keys(self._page.edit_name, text) 
        time.sleep(1)

    def click_save_button(self):
        self.click(self._page.save_button)

    def cancel_edit_button(self):
        time.sleep(1)
        self.click(self._page.cancel_edit_button)

    def click_delete_button(self):
        time.sleep(1)
        delete_button = self.find_element(*self._page.delete_button)
        self.action_catena(delete_button, "单击")

    def cancel_delete_button(self):
        time.sleep(1)
        self.click(self._page.cancel_delete_button)   

    def get_manage_deleted_users_model(self):
        return self.find_element(*self._page.manage_deleted_users_model).get_attribute("aria-label")

    def get_search_input_exist_user(self):
        return self.is_element_present(self._page.exist_user)

    def get_edit_button(self):
        return self.find_element(*self._page.edit_button).get_attribute("xlink:href")

    def get_save_button(self):
        return self.find_element(*self._page.save_button).is_enabled()

    def get_cancel_edit_button(self):
        return self.find_element(*self._page.cancel_edit_button).is_enabled()

    def get_delete_button(self):
        return self.find_element(*self._page.delete_button).get_attribute("xlink:href")

    def get_cancel_delete_button(self):
        return self.find_element(*self._page.cancel_delete_button).is_enabled()

    # 再次封装，执行所有操作
    # def all_actions(self, search_text, edit_text):
    #     self.search_deleted_users(search_text)
    #     self.click_edit_button()
    #     self.edit_user_name(edit_text)
    #     self.click_save_button()
    #     self.cancel_edit_button()
    #     self.click_delete_button()
    #     self.cancel_delete_button()