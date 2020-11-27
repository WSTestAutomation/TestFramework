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

    # 获取元素点击按钮
    def settings_element(self, sname):
        if self.is_element_clickable(sname):
            self.click(sname)
        else:
            element = self.find_element(*sname)
            self.perform_javascript_click(element)
 
    # 点击admin_settings按钮
    def click_admin_link(self):
        self.settings_element(self._page.setting_button)
        self.settings_element(self._page.adminsettings_link)
    
    # 进入admin_settings页面
    def admin_settings_page(self):
        self.settings_element(self._page.manage_deleted_users)
        
    def search(self, text):
        self.send_keys(self._page.search_delete_users, text)
        self.click(self._page.search_button)
        






        


        


    