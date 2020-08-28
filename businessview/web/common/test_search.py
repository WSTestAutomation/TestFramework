# coding=utf-8

from baseview.web.base_web import BaseWebPage
from page.web.business_page import BusinessPage as Page
from utilstest.base_yaml import Yaml
from utilstest.dynamic_loading import dynamic_loading
from common.browser_engine import Logger

class SearchBusiness(BaseWebPage):

    def __init__(self, driver):
        BaseWebPage.__init__(self=self, driver=driver)
        self._page = Page()

    def test_search(self):
        is_sucess = False
        Logger.info('test_search')
        try:
            self.send_keys(self._page.search_input, 'test', need_enter=True)
            element = self.find_elements_by_xpath(self._page.check_search_content_column)
            _dynamic_loading = dynamic_loading(driver=self.driver)
            _dynamic_loading.loading()

            getTitleText = self.find_elements_by_xpath(self._page.check_title_text)

            for i in getTitleText:
                Logger.info(i.text)
                if 'test' not in i.text and 'Test' not in i.text:
                    # ele = self.find_elements_by_text(i.text)
                    # getDescriptionText = self.find_elements_by_xpath(self._page.check_description_text)
                    ele = self.find_element_by_text(self._page.check_title_text, i.text)
                    print(ele)
                    print(ele.text)
                    print(type(ele))

                    return is_sucess

            is_sucess = True
        except Exception as e:
            Logger.error('Exception: %s', format(e))
        finally:
            return is_sucess