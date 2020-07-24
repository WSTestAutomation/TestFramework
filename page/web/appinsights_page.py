# coding=utf-8

from page.web.base_page import BasePage
from selenium.webdriver.common.by import By


class AiPage(BasePage):
    application_insights = (By.LINK_TEXT, 'Application Insights')
    add_button = (By.CSS_SELECTOR, 'div[title="New Application Insights"]')
    subscription_region = (By.CSS_SELECTOR, 'input.fxc-inputhasvalue')
    resource_group = (By.CSS_SELECTOR, 'input[placeholder="Select existing..."]')
    instance_name = (By.CSS_SELECTOR, '.fxc-section-control.msportalfx-form-formelement.azc-textField')
    input_box = (By.CSS_SELECTOR, 'input.azc-input')
    progress_status = (By.CSS_SELECTOR, 'a.fxs-toast-title.fxs-toast-link')
    toolbar_button = (By.CSS_SELECTOR, 'div.azc-toolbarButton-container.fxs-portal-hover')
    wait_review = (By.CSS_SELECTOR, 'span.fxs-blade-status-text')
    filter_name = (By.CSS_SELECTOR, '[placeholder="Filter by name..."]')
    context_menu = (By.CSS_SELECTOR, '[title="Click to open context menu"]')
    context_menu_pin = (By.CSS_SELECTOR, '.fxs-contextMenu-item.msportalfx-command-like-button.fxs-portal-hover')
    context_menu_delete = (By.CSS_SELECTOR, '.fxs-contextMenu-item.msportalfx-command-like-button.fxs-contextMenu-extensioncommand.fxs-portal-hover')
    yes_button = (By.CSS_SELECTOR, '[title="Yes"]')
    popup_message = (By.CSS_SELECTOR, 'div.fxs-progressbox-progressbar')
    empty_title = (By.CSS_SELECTOR, 'h2.ext-hubs-browse-emptytitle')
    delete_ai_blade = (By.CSS_SELECTOR, 'div.fxs-contextpane-visible')

