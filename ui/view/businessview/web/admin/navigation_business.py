# coding=utf-8
# @Time    :
# @Author  :
# @File    : navigation_business.py

from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.admin.navigation_page import NavigationPage as Page
from ui.lib.browser_engine import Logger

class Navigation_business(BusinessWebPage):
    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()
        self.managestream_menu_dict = {
                                        'Administrators':   self._page.managestream_administrators_button,
                                        'Spotlight videos': self._page.managestream_spotlight_videos_button,
                                        'Company policies':   self._page.managestream_company_policies_button,
                                        'Usage details':   self._page.managestream_usage_details_button,
                                        'Recycle bin':   self._page.managestream_recycle_bin_button,
                                        'Groups':   self._page.managestream_groups_button,
                                        'Support':   self._page.managestream_support_button,
                                        'Comments':   self._page.managestream_comments_button,
                                        'Content creation':   self._page.managestream_content_creation_button,
                                        'eCDN solutions':   self._page.managestream_eCDN_solutions_button
                                        }
        self.streammigration_menu_dict = {
                                            'Enable migration':   self._page.streammigration_enable_migration_button
                                        }
        self.dataprivacy_menu_dict = {
                                    'Manage user data':   self._page.dataprivacy_manage_user_data_button,
                                    'Manage deleted users':   self._page.dataprivacy_manage_deleted_users_button
                                     }
        self.tabpage_dict = {
            'Administrators':   self._page.tabpage_administrators_page,
            'Spotlight videos':   self._page.tabpage_spotlight_videos_page,
            'Company policies':   self._page.tabpage_company_policies_page,
            'Usage details':   self._page.tabpage_usage_details_page,
            'Recycle bin':   self._page.tabpage_recycle_bin_page,
            'Groups':   self._page.tabpage_groups_page,
            'Support':   self._page.tabpage_support_page,
            'Comments':   self._page.tabpage_comments_page,
            'Content creation':   self._page.tabpage_content_creation_page,
            'eCDN solutions':   self._page.tabpage_eCDN_solutions_page,
            'Enable migration':   self._page.tabpage_enable_migration_page,
            'Manage user data':   self._page.tabpage_manage_user_data_page,
            'Manage deleted users':   self._page.tabpage_manage_deleted_users_page
        }
    def tabpage_is_element_present(self,pname):
        self.is_element_present(pname)

    def click_navigation_button(self, fname):
        if self.is_element_clickable(fname):
            self.click(fname)
        else:
            element = self.find_element(*fname,timeout=3)
            self.perform_javascript_click(element)

    def adminsettings_is_element_present(self):
        self.is_element_present(self._page.adminsettings_tab)

    def click_navigation_button_managestream(self):
        self.click_navigation_button(self._page.managestream_button)        

    def click_navigation_button_streammigration(self):
        self.click_navigation_button(self._page.streammigration_button)

    def click_navigation_button_dataprivacy(self):
        self.click_navigation_button(self._page.dataprivacy_button)