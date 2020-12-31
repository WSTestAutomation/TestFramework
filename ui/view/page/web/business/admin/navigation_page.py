# coding=utf-8
# @Time    :
# @Author  :
# @File    : navigation_page.py

from selenium.webdriver.common.by import By

class NavigationPage:

    error_box = (By.XPATH, '//error-box')
    
    #tab
    adminsettings_tab = (By.XPATH, '//div[contains(@class, "top-header ng-binding")]')
    #Manage Stream
    managestream_button = (By.XPATH, '//button[contains(@aria-controls, "manage-stream-navigation")]')
    managestream_administrators_button = (By.XPATH, '//button[text()=" Administrators "]')
    managestream_spotlight_videos_button = (By.XPATH, '//button[text()=" Spotlight videos "]')
    managestream_company_policies_button = (By.XPATH, '//button[text()=" Company policies "]')
    managestream_usage_details_button = (By.XPATH, '//button[text()=" Usage details "]')
    managestream_recycle_bin_button = (By.XPATH, '//button[text()=" Recycle bin "]')
    managestream_groups_button = (By.XPATH, '//button[text()=" Groups "]')
    managestream_support_button = (By.XPATH, '//button[text()=" Support "]')
    managestream_comments_button = (By.XPATH, '//button[text()=" Comments "]')
    managestream_content_creation_button = (By.XPATH, '//button[text()=" Content creation "]')
    managestream_eCDN_solutions_button = (By.XPATH, '//button[text()=" eCDN solutions "]')
    #Sream Migration
    streammigration_button = (By.XPATH, '//button[contains(@aria-controls, "manage-stream-migration-navigation")]')
    streammigration_enable_migration_button = (By.XPATH, '//button[text()=" Enable migration "]')
    #Data Privacy
    dataprivacy_button = (By.XPATH, '//button[contains(@aria-controls, "manage-users-navigation")]')
    dataprivacy_manage_user_data_button = (By.XPATH, '//button[text()=" Manage user data "]')
    dataprivacy_manage_deleted_users_button = (By.XPATH, '//button[text()=" Manage deleted users "]')

    #tab page
    tab_page = (By.XPATH, '//div[contains(@class, "tab-page")]')
    tab_page_administrators = (By.XPATH, '//div[contains(@class, "tab-page")]/assign-admins')
    tab_page_spotlight_videos = (By.XPATH, '//div[contains(@class, "tab-page")]/spotlight-videos')
    tab_page_company_policies = (By.XPATH, '//div[contains(@class, "tab-page")]/company-policies')
    tab_page_usage_details = (By.XPATH, '//div[contains(@class, "tab-page")]/usage-details')
    tab_page_recycle_bin = (By.XPATH, '//div[contains(@class, "tab-page")]/recycle-bin')
    tab_page_groups = (By.XPATH, '//div[contains(@class, "tab-page")]/groups')
    tab_page_support = (By.XPATH, '//div[contains(@class, "tab-page")]/support')
    tab_page_comments = (By.XPATH, '//div[contains(@class, "tab-page")]/comments-management')
    tab_page_content_creation = (By.XPATH, '//div[contains(@class, "tab-page")]/content-creation')
    tab_page_eCDN_solutions = (By.XPATH, '//div[contains(@class, "tab-page")]/network-caching')
    tab_page_enable_migration = (By.XPATH, '//div[contains(@class, "tab-page")]/enable-migration')
    tab_page_manage_user_data = (By.XPATH, '//div[contains(@class, "tab-page")]/personal-data')
    tab_page_manage_deleted_users = (By.XPATH, '//div[contains(@class, "tab-page")]/forgotten-users')
