# coding=utf-8
# @Time    :
# @Author  :
# @File    : navigation_business.py

from selenium.webdriver.common.by import By
from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.admin.navigation_page import NavigationPage as Page

class Navigation_business(BusinessWebPage):

    class Admin_settings_menu_item():
        def __init__(self, obj, name='', has_subitems=False, parent=None, is_clickable=False, by=None, tab_by=None):
            self.name = name
            self.has_subitems = has_subitems
            self.parent = parent
            self.is_clickable = is_clickable
            self.by = by
            self.tab_by = tab_by
            self.obj = obj

        def click(self):
            if self.obj.is_element_clickable(self.by):
                self.obj.click(self.by)
                return True
            return False
        
        def is_present(self):
            return self.obj.is_element_present(self.by)

        def is_expanded(self):
            if self.has_subitems is False:
                return False

            is_expanded = False
            # 检查子节点是否显示，或者通过其他手段
            # 1. 元素的 aria-expanded 属性需要是true
            # 2. 对应的<tab-navigation> 元素的style属性需要是"display: inline;", 可以通过元素的aria-controls属性获取id
            element_self = self.obj.find_element(*self.by)
            check_point_1 = element_self.get_attribute("aria-expanded").lower() == "true"

            element_tab_navigation = self.obj.find_element(*(By.ID, element_self.get_attribute("aria-controls")))
            check_point_2 = element_tab_navigation.get_attribute("style").lower() in ("display: inline;", "")

            is_expanded = check_point_1 and check_point_2

            return is_expanded

        """
        展开子项目
        """
        def expand(self):
            obj = self.obj
            if self.is_expanded():
                return True
            if self.has_subitems:
                try:
                    if obj.is_element_clickable(self.by):
                        obj.click(self.by)
                    else:
                        element = obj.find_element(*self.by, timeout=3)
                        obj.perform_javascript_click(element)
                except Exception as e:
                    print("展开'%s'出现问题：%s" & (self.name, format(e)))
            # 检验效果
            is_sucess = self.is_expanded()
            return is_sucess

        """
        隐藏子项目
        """
        def contract(self):
            obj = self.obj
            if not(self.is_expanded()):
                return True
            if self.has_subitems:
                try:
                    if obj.is_element_clickable(self.by):
                        obj.click(self.by)
                    else:
                        element = obj.find_element(*self.by, timeout=3)
                        obj.perform_javascript_click(element)
                except Exception as e:
                    print("收起'%s'出现问题：%s" & (self.name, format(e)))
            # 检验效果
            is_sucess = not(self.is_expanded())
            return is_sucess

    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()
        self.menu = {
            'Admin settings': self.Admin_settings_menu_item(name="Admin settings", obj=self, has_subitems=False, parent=None, is_clickable=False, by=self._page.adminsettings_tab, tab_by=None),
            'Manage Stream': self.Admin_settings_menu_item(name="Manage Stream", obj=self, has_subitems=True, parent=None, is_clickable=True, by=self._page.managestream_button, tab_by=None),
            'Administrators': self.Admin_settings_menu_item(name="Administrators", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_administrators_button, tab_by=self._page.tab_page_administrators),
            'Spotlight videos': self.Admin_settings_menu_item(name="Spotlight videos", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_spotlight_videos_button, tab_by=self._page.tab_page_spotlight_videos),
            'Company policies': self.Admin_settings_menu_item(name="Company policies", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_company_policies_button, tab_by=self._page.tab_page_company_policies),
            'Usage details': self.Admin_settings_menu_item(name="Usage details", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_usage_details_button, tab_by=self._page.tab_page_usage_details),
            'Recycle bin': self.Admin_settings_menu_item(name="Recycle bin", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_recycle_bin_button, tab_by=self._page.tab_page_recycle_bin),
            'Groups': self.Admin_settings_menu_item(name="Groups", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_groups_button, tab_by=self._page.tab_page_groups),
            'Support': self.Admin_settings_menu_item(name="Support", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_support_button, tab_by=self._page.tab_page_support),
            'Comments': self.Admin_settings_menu_item(name="Comments", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_comments_button, tab_by=self._page.tab_page_comments),
            'Content creation': self.Admin_settings_menu_item(name="Content creation", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_content_creation_button, tab_by=self._page.tab_page_content_creation),
            'eCDN solutions': self.Admin_settings_menu_item(name="eCDN solutions", obj=self, has_subitems=False, parent='Manage Stream', is_clickable=True, by=self._page.managestream_eCDN_solutions_button, tab_by=self._page.tab_page_eCDN_solutions),
            'Manage Stream':self.Admin_settings_menu_item(name="Manage Stream", obj=self, has_subitems=True, parent=None, is_clickable=True, by=self._page.streammigration_button, tab_by=None),
            'Enable migration': self.Admin_settings_menu_item(name="Enable migration", obj=self, has_subitems=False, parent='Stream Migration', is_clickable=True, by=self._page.streammigration_enable_migration_button, tab_by=self._page.tab_page_enable_migration),
            'Data Privacy':self.Admin_settings_menu_item(name="Data Privacy", obj=self, has_subitems=True, parent=None, is_clickable=True, by=self._page.dataprivacy_button, tab_by=None),
            'Manage user data': self.Admin_settings_menu_item(name="Manage user data", obj=self, has_subitems=False, parent='Data Privacy', is_clickable=True, by=self._page.dataprivacy_manage_user_data_button, tab_by=self._page.tab_page_manage_user_data),
            'Manage deleted users': self.Admin_settings_menu_item(name="Manage deleted users", obj=self, has_subitems=False, parent='Data Privacy', is_clickable=True, by=self._page.dataprivacy_manage_deleted_users_button, tab_by=self._page.tab_page_manage_deleted_users)
        }

    def is_sign_in_successully(self):
        
        if self.driver is None:
            return False
        # 假如有错误，如：权限问题
        try:
            error_box = self.find_element(self._page.error_box)
            error_msg = error_box.get_attribute('title-str')
            print("Failing to view the webpage: "+ error_msg)
            return False
        except:
            # fine to have no error. :)
            pass
        
        try:
            self.find_element(*self._page.adminsettings_tab)
            return True
        except:
            return False

    def get_elements_under_tab_page(self):
        tab_page = self.find_element(*self._page.tab_page)
        return tab_page.find_elements_by_xpath("*")