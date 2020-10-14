# coding=utf-8

from selenium.webdriver.common.by import By


class BasePage:
    # 页面间常用的元素，需要结合项目做更改
    # 以下是示例
    next_button = (By.CSS_SELECTOR, 'input[value="Next"]')
    sign_button = (By.CSS_SELECTOR, 'span[class="submit"]')
    yes_button = (By.CSS_SELECTOR, 'input[value="Yes"]')
    no_button = (By.CSS_SELECTOR, 'input[value="No"]')
