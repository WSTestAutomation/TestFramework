# coding=utf-8
# @Time    :
# @Author  :
# @File    : navigation_page.py

from selenium.webdriver.common.by import By

class NavigationPage:
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
    tabpage_administrators_page = (By.XPATH, '//div[contains(@class, "tab-page")]/assign-admins')
    tabpage_spotlight_videos_page = (By.XPATH, '//div[contains(@class, "tab-page")]/spotlight-videos')
    tabpage_company_policies_page = (By.XPATH, '//div[contains(@class, "tab-page")]/company-policies')
    tabpage_usage_details_page = (By.XPATH, '//div[contains(@class, "tab-page")]/usage-details')
    tabpage_recycle_bin_page = (By.XPATH, '//div[contains(@class, "tab-page")]/recycle-bin')
    tabpage_groups_page = (By.XPATH, '//div[contains(@class, "tab-page")]/groups')
    tabpage_support_page = (By.XPATH, '//div[contains(@class, "tab-page")]/support')
    tabpage_comments_page = (By.XPATH, '//div[contains(@class, "tab-page")]/comments-management')
    tabpage_content_creation_page = (By.XPATH, '//div[contains(@class, "tab-page")]/content-creation')
    tabpage_eCDN_solutions_page = (By.XPATH, '//div[contains(@class, "tab-page")]/network-caching')
    tabpage_enable_migration_page = (By.XPATH, '//div[contains(@class, "tab-page")]/enable-migration')
    tabpage_manage_user_data_page = (By.XPATH, '//div[contains(@class, "tab-page")]/personal-data')
    tabpage_manage_deleted_users_page = (By.XPATH, '//div[contains(@class, "tab-page")]/forgotten-users')
