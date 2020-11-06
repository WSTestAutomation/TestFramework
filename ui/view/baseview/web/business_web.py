# coding=utf-8

import logging
import random
from ui.view.baseview.web.base_web import BaseWebPage, time
from ui.view.page.web.business.common.business_page import BusinessPage


class BusinessWebPage(BaseWebPage):
    def __init__(self, driver):
        BaseWebPage.__init__(self, driver)
        self._page = BusinessPage()


"""
    def _switch_info_window(self, handle, message="处理成功！", wait_time=None, is_pass=False):
        logging.info('处理信息反馈')
        if wait_time is not None:
            time.sleep(wait_time)
        self.switch_to_window(self._page.system_info_window_name)
        comment = self.find_element(*self._page.feedback_common).text
        if is_pass:
            pass
        else:
            assert comment == message
        ele = self.driver.find_element(*self._page.feedback_submit_button)
        ele.click()
        self.switch_to_window(handle)
        self.switch_to_frame(self._page.iframe_id)

    def select_options_by_value(self, double_element_loc, value, wait_time=3):
        self.double_click(double_element_loc)
        time.sleep(wait_time)
        element = self.find_element(*self._page.code_select)
        self._select_options_by_value(element, value)

    def select_options_by_random(self, double_element_loc, wait_time=2):
        self.double_click(double_element_loc)
        time.sleep(wait_time)
        element = self.find_element(*self._page.code_select)
        options = self._get_select_options(element)
        value = random.choice(options).get_attribute('value')
        self._select_options_by_value(element, value)


    def accept_alert_message(self, message):
        logging.info('处理弹出')
        alert_box = self.switch_to_alert()
        assert alert_box.text == message
        alert_box.accept()

    def dismiss_alert_message(self, message):
        logging.info('取消弹窗')
        alert_box = self.switch_to_alert()
        assert alert_box.text == message
        alert_box.dismiss()
"""