# coding=utf-8
# @Time    :
# @Author  :
# @File    : business_page.py

from selenium.webdriver.common.by import By

class SearchPage:
    first_search_input = (By.XPATH, '//input[@aria-label="Enter your search"]')
    search_input = (By.XPATH, '//input[@placeholder="Search for videos ..."]')
    check_title_text = ('//span[contains(@class= "-title ng-binding ng-isolate-scope")]')
    check_people_title_text = ('//a[@class="person-card"]')
    check_description_text = (By.XPATH, '//div[@class="item-description-content ng-binding ng-scope"]')
    check_search_content_row = ('//div[@class="search-content row row-size0 column"]')
    check_search_result_if_null = ('//p[start-with(@class, "sub-text-container ng-binding")]')
    check_people_result_if_null = ('//div[@class="column ng-binding"]')
    click_first_video = (By.XPATH, '//span[contains(@class= "-title ng-binding ng-isolate-scope")]')
    click_first_people = (By.XPATH, '//a[@class="person-card"]')
    click_channels_button = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-1"]')
    click_People_button = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-2"]')
    check_search_for_text = ('//label[@class="c-label ng-binding"]')
    my_content_column = (By.XPATH, '//span[@class="link-label ng-binding"]')
    my_content_video = (By.XPATH, '/a[@class="my-video-link"]')
    my_content_channels = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-1"]')
    check_my_content_result_if_null = ('//div[@class="ng-binding ng-scope"]')
    my_content_my_watchlists = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-3"]')
    my_content_my_followed = (By.XPATH, '//button[@class="c-action-trigger nav-link nav-link-option-4"]')