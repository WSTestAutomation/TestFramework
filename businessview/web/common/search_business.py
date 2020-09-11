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
            getSearchResult = self.find_elements_by_xpath(self._page.check_my_content_result_if_null)
            for i in getSearchResult:
                if "There are no " in i.text:
                    Logger.info('There are no videos to display')
                    return is_sucess

        if (navigationTopBar == "Videos" or navigationTopBar == "channels" or navigationTopBar == "followed") and (Browser == "Discover"or Browser == "My content folloewd"):
            getSearchResult = self.find_elements_by_xpath(self._page.check_search_result_if_null)
            for i in getSearchResult:
                if "There are no " in i.text:
                    Logger.info('There are no videos to display')
                    return is_sucess

        if (navigationTopBar == "People") and Browser == "Discover":
            getSearchResult = self.find_elements_by_xpath(self._page.check_people_result_if_null)
            for i in getSearchResult:
                if "There are no people to display" in i.text:
                    Logger.info('There are no people to display')
                    return is_sucess
        try:
            element = self.find_elements_by_xpath(self._page.check_search_content_row)
            _dynamic_loading = dynamic_loading(driver=self.driver)
            _dynamic_loading.loading()

            # if navigationTopBar == "Videos" or navigationTopBar == "channels" or navigationTopBar == "watchlists" or navigationTopBar == "followed":
            #     getTitleText = self.find_elements_by_xpath(self._page.check_title_text)
            # if navigationTopBar == "People"
            #     getTitleText = self.find_elements_by_xpath(self._page.check_people_title_text)

            if navigationTopBar == "People":
                getTitleText = self.find_elements_by_xpath(self._page.check_people_title_text)
            else:
                getTitleText = self.find_elements_by_xpath(self._page.check_title_text)
            
            for i in getTitleText:
                Logger.info(i.text)
                if 'test' not in i.text and 'Test' not in i.text:
                    pass
                    # ele = self.find_elements_by_text(i.text)
                    # getDescriptionText = self.find_elements_by_xpath(self._page.check_description_text)
                    # ele = self.find_element_by_text(self._page.check_title_text, i.text)
                    # print(ele)
                    # print(ele.text)
                    # print(type(ele))
                
            is_sucess = True
        except Exception as e:
            Logger.error('Exception: %s', format(e))
        finally:
            return is_sucess
        

    def search_for_videos(self, text, navigationTopBar, changeSortMode, Browser="Discover", firstSearch=False):
        if firstSearch == True:
            self.send_keys(self._page.first_search_input, text, need_clear=True, need_enter=True)
        else:
            self.send_keys(self._page.search_input, text, need_clear=True, need_enter=True)
        getResult = self.check_search_result(navigationTopBar, Browser)
        if getResult:
            if changeSortMode == True:
                change_sort_mode()
            if navigationTopBar == "Videos" or navigationTopBar == "channels" or navigationTopBar == "watchlists":
                self.clicks(self._page.click_first_video, 0)
                self.check_currunt_page()
            if navigationTopBar == "People":
                 self.clicks(self._page.click_first_people, 0)
                 self.check_currunt_page()
        
        self.click_back_button()
        self.check_currunt_page()

    