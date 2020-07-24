# coding=utf-8

import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from baseview.web.base_web import BaseWebPage
from page.web.appinsights_page import AiPage as Page


class AiBusiness(BaseWebPage):

    def __init__(self, driver):
        BaseWebPage.__init__(self=self, driver=driver)
        self._page = Page()
        self.ai_name = 'test{}'.format(time.strftime('%Y%m%d%H%M%S', time.localtime()))

    def create_ai(self):
        self.click(self._page.application_insights)
        self.find_element(*self._page.wait_loading)
        self.click(self._page.add_button)
        self.clicks(self._page.subscription_region, 0)
        self.find_element_click(self._page.option, 'AI - APM - Perf')
        time.sleep(1)
        self.send_keys(self._page.resource_group, 'AIUIAutomation', need_enter=True)
        instance_name = self.find_element(*self._page.instance_name)
        input_name = instance_name.find_element(*self._page.input_box)
        input_name.send_keys(self.ai_name)
        self.clicks(self._page.subscription_region, 3)
        self.find_element_click(self._page.option, '(US) South Central US')
        self.find_element_click(self._page.simple_button, 'Review + create')
        self.wait_review(self._page.wait_review, 'Validation passed')
        self.find_element_click(self._page.simple_button, 'Create')
        self.wait_loading(self._page.wait_notifications)
        deployment_status = self.find_element(*self._page.progress_status)
        return deployment_status

    def delete_ai(self):
        self.find_element_click(self._page.simple_button, 'Go to resource')
        self.wait_disappear(self._page.progress_dots)
        toolbar = self.find_element(*self._page.toolbar_container)
        delete_button = toolbar.find_element(*self._page.delete_button)
        delete_button.click()
        delete_ai_blade = self.find_element(*self._page.delete_ai_blade)
        input_box = delete_ai_blade.find_element(*self._page.input_box)
        input_box.send_keys(self.ai_name)
        time.sleep(2)
        button = delete_ai_blade.find_elements(*self._page.simple_button)
        button[0].click()
        self.wait_loading(self._page.wait_notifications)
        delete_status = self.find_element(*self._page.progress_status)
        return delete_status

    # two the way of delete AI
    # def delete_ai(self):
    #     time.sleep(40)  # wait create AI load completed
    #     self.click(self._page.topbar_sidebar)
    #     self.click(self._page.application_insights)
    #     self.find_element(*self._page.wait_loading)
    #     self.send_keys(self._page.filter_name, self.ai_name)
    #     time.sleep(3)
    #     context_menu = self.find_element(*self._page.context_menu)
    #     self.action_catena(context_menu, '右击')
    #     delete_button = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self._page.context_menu_delete))
    #     delete_button.click()
    #     self.click(self._page.yes_button)
    #     deleting = self.find_element(*self._page.popup_message)
    #     assert '50% complete' in deleting.text
    #     if deleting is not None:
    #         WebDriverWait(self.driver, 30).until_not(EC.presence_of_element_located(self._page.popup_message))
    #         empty_title = self.find_element(*self._page.empty_title)
    #         assert 'No Application Insights app to display' in empty_title.text
    #     else:
    #         raise Exception("delete ai not succeed.")

    def wait_review(self, loc, text):
        elements = self.find_elements(*loc)
        for element in elements:
            if text in element.text:
                return element
            else:
                time.sleep(5)

    def wait_loading(self, loc):
        time.sleep(1)
        WebDriverWait(self.driver, 180).until(EC.presence_of_element_located(locator=loc))

    def wait_disappear(self, loc):
        WebDriverWait(self.driver, 30).until_not(EC.presence_of_element_located(locator=loc))

