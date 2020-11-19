# coding=utf-8

from ui.view.baseview.web.business_web import BusinessWebPage
from ui.view.page.web.business.common.search_page import SearchPage as Page
from ui.lib.dynamic_loading import dynamic_loading
from ui.lib.browser_engine import Logger
#import time

class SearchBusiness(BusinessWebPage):

    def __init__(self, driver):
        BusinessWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def check_currunt_page(self):
        # TODO: Do some operations/validations here
        #time.sleep(5)
        pass

    def change_sort_mode(self):
        # TODO: Do some operations/validations here
        pass

    def check_search_result(self, navigationTopBar, Browser):
        # TODO: Need to update

        is_sucess = False
        if Browser == "My content Channels" or Browser == "My content My watchlists":
            getSearchResult = self.is_element_present(self._page.check_my_content_result_if_null)
            if getSearchResult == True:
                return is_sucess

        if (navigationTopBar == "Videos" or navigationTopBar == "Channels" or navigationTopBar == "followed") and (Browser == "Discover"or Browser == "My content folloewd"):
            getSearchResult = self.is_element_present(self._page.check_search_result_if_null)
            if getSearchResult == True:
                return is_sucess

        if (navigationTopBar == "People") and Browser == "Discover":
            getSearchResult = self.is_element_present(self._page.check_people_result_if_null)
            if getSearchResult == True:
                return is_sucess
        try:
            _dynamic_loading = dynamic_loading(driver=self.driver)
            _dynamic_loading.loading()

            if navigationTopBar == "People":
                getTitleText = self.find_elements(*self._page.check_people_title_text)
            elif Browser == "My content Channels" and navigationTopBar == "Channels":
                getTitleText = self.find_elements(*self._page.check_my_content_channels_title_text)
            else:
                getTitleText = self.find_elements(*self._page.check_title_text)

            for i in getTitleText:
                Logger.info(i.text)
                if 'test' not in i.text and 'Test' not in i.text:
                    pass

            is_sucess = True
        except Exception as e:
            Logger.error('Exception: %s', format(e))
        finally:
            return is_sucess


    def search_for_videos(self, text, navigationTopBar, changeSortMode=False, Browser="Discover", firstSearch=False):
        # TODO: Need to update

        if firstSearch == True:
            self.send_keys(self._page.first_search_input, text, need_clear=True, need_enter=True)
        else:
            self.send_keys(self._page.search_input, text, need_clear=True, need_enter=True)
        getResult = self.check_search_result(navigationTopBar, Browser)
        if getResult:
            _dynamic_loading = dynamic_loading(driver=self.driver)
            _dynamic_loading.scrool_top()
            if changeSortMode == True:
                self.change_sort_mode()
            if navigationTopBar == "People":
                self.clicks(self._page.check_people_title_text, 0)
                self.check_currunt_page()
            elif Browser == "My content Channels" and navigationTopBar == "Channels":
                self.clicks(self._page.check_my_content_channels_title_text, 0)
                self.check_currunt_page()
            else:
                self.clicks(self._page.check_title_text, 0)
                self.check_currunt_page()

        self.click_back_button()
        self.check_currunt_page()
    