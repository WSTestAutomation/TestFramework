# coding=utf-8
# @Time    :
# @Author  :
# @File    : business_page.py

from selenium.webdriver.common.by import By
from ui.view.page.web.base.base_page import BasePage

class BusinessPage:
    submit_button = (By.ID, 'submit2')
    add_info_button = (By.CSS_SELECTOR, 'input[value="新  增"]')
    