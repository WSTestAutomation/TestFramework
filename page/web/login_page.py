# coding=utf-8

from page.web.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    user_name_input = (By.NAME, 'loginfmt')
    password_input = (By.NAME, 'passwd')
    signin_input = (By.XPATH,'//input[@value="Sign in"]')


