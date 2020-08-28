# coding=utf-8
# @Time    :
# @Author  :
# @File    : business_page.py

from selenium.webdriver.common.by import By


class BusinessPage:
    submit_button = (By.ID, 'submit2')
    add_info_button = (By.CSS_SELECTOR, 'input[value="新  增"]')
    search_input = (By.XPATH, '//input[@aria-label="Enter your search"]')
    check_title_text = ('//span[@class="video-title ng-binding ng-isolate-scope"]')
    check_description_text = (By.XPATH, '//div[@class="item-description-content ng-binding ng-scope"]')
    check_search_content_column = ('//div[@class="search-content row row-size0 column"]')

    class_Text = ('//div[@class="name-description ng-scope"]')
