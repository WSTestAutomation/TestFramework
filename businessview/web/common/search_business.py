# coding=utf-8

from baseview.web.base_web import BaseWebPage
from page.web.search_page import SearchPage as Page
from utilstest.dynamic_loading import dynamic_loading
from common.browser_engine import Logger

class SearchBusiness(BaseWebPage):

    def __init__(self, driver):
        BaseWebPage.__init__(self=self, driver=driver)
        self._page = Page()
    
    def check_currunt_page(self):
        pass

    def change_sort_mode(self):
        pass

    def check_search_result(self, navigationTopBar, Browser):
        is_sucess = False
        if Browser == "My content Channels" or Browser == "My content My watchlists":
            getSearchResult = self.check_element_if_present(self._page.check_my_content_result_if_null)
            if getSearchResult == "True":
                return is_sucess

        if (navigationTopBar == "Videos" or navigationTopBar == "channels" or navigationTopBar == "followed") and (Browser == "Discover"or Browser == "My content folloewd"):
            getSearchResult = self.check_element_if_present(self._page.check_search_result_if_null)
            if getSearchResult == "True":
                return is_sucess

        if (navigationTopBar == "People") and Browser == "Discover":
            getSearchResult = self.check_element_if_present(self._page.check_people_result_if_null)
            if getSearchResult == "True":
                return is_sucess
        try:
            _dynamic_loading = dynamic_loading(driver=self.driver)
            _dynamic_loading.loading()

            if navigationTopBar == "People":
                getTitleText = self.find_elements(*self._page.check_people_title_text)
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
            if navigationTopBar == "Videos" or navigationTopBar == "channels" or navigationTopBar == "watchlists":
                self.clicks(self._page.click_a_video, 0)
                self.check_currunt_page()
            if navigationTopBar == "People":
                 self.clicks(self._page.click_a_people, 0)
                 self.check_currunt_page()
        
        self.click_back_button()
        self.check_currunt_page()

    