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
                                        'Administrators':   self._page.managestream_Administrators_button,
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
                                            'Enable migration':   self._page.streammigration_enablemigration_button
                                        }
        self.dataprivacy_menu_dict = {
                                    'Manage user data':   self._page.dataprivacy_manage_user_data_button,
                                    'Manage deleted users':   self._page.dataprivacy_manage_deleted_users_button
                                     }

    def click_navigation_button(self, fname):
        if self.is_element_clickable(fname):
            self.click(fname)
        else:
            element = self.find_element(*fname,timeout=3)
            self.perform_javascript_click(element)

    def adminsettings_is_element_clickable(self):
        self.is_element_present(self._page.adminsettings_tab)

    def click_navigation_button_managestream(self):
        self.click_navigation_button(self._page.managestream_button)        

    def click_navigation_button_streammigration(self):
        self.click_navigation_button(self._page.streammigration_button)

    def click_navigation_button_dataprivacy(self):
        self.click_navigation_button(self._page.dataprivacy_button)