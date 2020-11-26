# coding=utf-8
# @Time    :
# @Author  :
# @File    : navigation_page.py

from selenium.webdriver.common.by import By

class NavigationPage:
    adminsettings_tab = (By.XPATH, '//div[contains(@class, "top-header ng-binding")]')

    #Manage Stream
    managestream_button = (By.XPATH, '//button[contains(@aria-controls, "manage-stream-navigation")]')
    managestream_Administrators_button = (By.XPATH, '//button[text()=" Administrators "]')
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
    streammigration_enablemigration_button = (By.XPATH, '//button[text()=" Enable migration "]')

    #Data Privacy
    dataprivacy_button = (By.XPATH, '//button[contains(@aria-controls, "manage-users-navigation")]')
    dataprivacy_manage_user_data_button = (By.XPATH, '//button[text()=" Manage user data "]')
    dataprivacy_manage_deleted_users_button = (By.XPATH, '//button[text()=" Manage deleted users "]')
