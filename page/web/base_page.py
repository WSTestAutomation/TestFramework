# coding=utf-8

from selenium.webdriver.common.by import By


class BasePage:
    next_button = (By.CSS_SELECTOR, 'input[value="Next"]')
    sign_button = (By.CSS_SELECTOR, 'span[class="submit"]')
    simple_button = (By.CSS_SELECTOR, 'span.fxs-button-text')
    yes_button = (By.CSS_SELECTOR, 'input[value="Yes"]')
    no_button = (By.CSS_SELECTOR, 'input[value="No"]')
    click_signin_button = (By.CSS_SELECTOR, 'p[class="normalText"]')
    header_title = (By.CSS_SELECTOR, 'header.fxs-home-title')
    option = (By.CSS_SELECTOR, 'span.fxs-portal-svg')
    wait_notifications = (By.CSS_SELECTOR, 'div.fxs-notificationspane-progressbar.fxs-display-none')
    wait_loading = (By.CSS_SELECTOR, '.fxs-bladecontent-progress.fxs-portal-background.fxs-display-none')
    topbar_sidebar = (By.CSS_SELECTOR, 'a.fxs-topbar-sidebar-collapse-button')
    toolbar_container = (By.CSS_SELECTOR, 'ul.azc-toolbar-container.fxs-commandBar-itemList')
    delete_button = (By.CSS_SELECTOR, 'li[title="Delete"]')
    blade_title = (By.CSS_SELECTOR, 'div.fxs-blade-title-content')
    progress_dots = (By.CSS_SELECTOR, 'fxs-progress-dots-dot')
    click_verify_button = (By.ID, 'WindowsAzureMultiFactorAuthentication')
    accountDetails_XPATH = '//div[@id="mectrl_currentAccount_secondary"]'
