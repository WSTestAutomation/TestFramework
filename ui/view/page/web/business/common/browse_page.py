# coding=utf-8
# @Time    :
# @Author  :
# @File    : browse_page.py

from selenium.webdriver.common.by import By

class BrowsePage:
    items_list = (By.XPATH, '//div[contains(@class, "items-list-container")]/div/child::div[contains(@ng-transclude, "item")]')
    items_list_container = (By.XPATH, '//items-list/div[contains(@class, "items-list-container")]')
    show_more_button = (By.XPATH, '//button[contains(@aria-label, "Show more")]')
