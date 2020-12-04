# coding=utf-8
# @Time    :
# @Author  :
# @File    : manage_deleted_users_business.py
import time
from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.admin.manage_deleted_users_page import ManageDeletedUserPage as Page
from ui.lib.browser_engine import Logger


class Manage_deleted_users_business(BusinessWebPage):
    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    # def is_enabled(self, loc):
    #     return self.find_element(*loc).is_enabled()

    # def get_attribute(self, loc, text):
    #     return self.find_element(*loc).get_attribute(text)

    def text(self, loc):
        return self.find_element(*loc).text

    def assert_edit(self):
        edit_button = self.text(self._page.edit_button)      
    
    # 点击settings按钮
    # def click_settings_button(self):
    #     time.sleep(2)
    #     self.click(self._page.setting_button)

    # 点击admin_settings按钮
    # def click_admin_link(self):
    #     element = self.find_element(*self._page.adminsettings_link)
    #     self.perform_javascript_click(element)
    #     time.sleep(1)
    #     self.switch_to_window_by_index(0)
    
    # 进入manage_deleted_users模块
    def admin_settings_page(self):
        self.click(self._page.manage_deleted_users)

    # find deleted users搜索框搜索
    def search(self, text):
        self.send_keys(self._page.search_delete_users, text)
        self.click(self._page.search_button)

    # click edit button
    def icon_edit(self):
        edit_button = self.find_element(*self._page.edit_button)
        self.action_catena(edit_button, "单击")

    # click delete button
    def delete_button(self):
        delete_button = self.find_element(*self._page.delete_button)
        self.action_catena(delete_button, "单击")

    # cancel delete
    def cancel_delete_button(self):
        self.click(self._page.cancel_delete_button)

    # input name --> sava
    def edit_user_details(self, text):
        self.send_keys(self._page.edit_name, text)
        self.click(self._page.save_edit_button)

    # cancel edit name
    def edit_cancel(self):
        self.icon_edit()
        time.sleep(1)
        self.click(self._page.cancel_edit_button)

    



    

        


        
        






        


        


    