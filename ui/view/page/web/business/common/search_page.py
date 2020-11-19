# coding=utf-8
# @Time    :
# @Author  :
# @File    : search_page.py

from ui.view.page.web.base.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage:
    first_search_input = (By.XPATH, '//input[@aria-label="Enter your search"]')
    search_input = (By.XPATH, '//input[contains(@placeholder, "Search for")]')
    check_title_text = (By.XPATH, '//span[contains(@class, "-title ng-binding ng-isolate-scope")]')
    check_my_content_channels_title_text = (By.XPATH, '//div[contains(@class, "-title ng-binding ng-isolate-scope")]')
    check_people_title_text = (By.XPATH, '//a[@class="person-card"]')
    check_description_text = (By.XPATH, '//div[@class="item-description-content ng-binding ng-scope"]')
    check_search_result_if_null = (By.XPATH, '//p[contains(@class, "sub-text-container ng-binding")]')
    check_people_result_if_null = (By.XPATH, '//div[@class="column ng-binding"]')
    click_channels_button = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-1"]')
    click_People_button = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-2"]')
    check_search_for_text = (By.XPATH, '//label[@class="c-label ng-binding"]')
    my_content_column = (By.XPATH, '//span[@class="link-label ng-binding"]')
    my_content_video = (By.XPATH, '//a[@class="my-video-link"]')
    my_content_channels = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-1"]')
    check_my_content_result_if_null = (By.XPATH, '//div[@class="ng-binding ng-scope"]')
    my_content_my_watchlists = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-3"]')
    my_content_my_followed = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-4"]')
    