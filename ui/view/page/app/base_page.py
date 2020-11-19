# coding=utf-8

from appium.webdriver.common.mobileby import MobileBy


class BasePage:
    select_env_text = (MobileBy.IOS_PREDICATE, 'value=="请输入"')
    confirm_btn = (MobileBy.ACCESSIBILITY_ID, '确定')
