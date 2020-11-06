# coding=utf-8
# @Time    :
# @Author  :
# @File    : login_page.py

from ui.view.page.web.base.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    user_name_input = (By.NAME, 'loginfmt')
    password_input = (By.NAME, 'passwd')
    next_input = (By.XPATH, '//input[@value="Next" or @value="下一步"]')
    signin_input = (By.XPATH, '//input[@value="Sign in" or @value="登录"]')
    yes_button = (By.XPATH, '//input[@value="Yes" or @value="是"]')
    no_button = (By.XPATH, '//input[@value="No" or @value="否"]')
