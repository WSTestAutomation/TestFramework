# coding=utf-8
# @Time    :
# @Author  :
# @File    : topbar_page.py

from selenium.webdriver.common.by import By

class TopbarPage:
    # O365 top bar
    appLauncher_button = (By.ID, 'O365_MainLink_NavMenu')
    appName_link = (By.ID, 'O365_AppName')
    featureFlags_button = (By.ID, 'O365_Feature_Flags')
    settings_button = (By.ID, 'O365_MainLink_Settings')
    help_button = (By.ID, 'O365_MainLink_Help')
    accountManager_button = (By.ID, 'mectrl_main_trigger')

    # Stream action bar
    home_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-home-button")]')
    discover_button = (By.ID, 'topbar-discover-navigation-button-desktop')
    discover_video_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-discover-video-link")]')
    discover_channel_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-discover-channel-link")]')
    discover_people_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-discover-people-link")]')
    discover_group_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-discover-group-link")]')
    myContent_button = (By.ID, 'topbar-mycontent-navigation-button-desktop')
    myContent_videos_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-myContent-videos-link")]')
    myContent_groups_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-myContent-groups-link")]')
    myContent_channels_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-myContent-channels-link")]')
    myContent_meetings_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-myContent-meetings-link")]')
    myContent_watchlist_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-myContent-watchlist-link")]')
    myContent_followed_channels_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-myContent-following-channels-link")]')
    myContent_recycle_bin_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-myContent-recycle-bin-link")]')
    create_button = (By.ID, 'create-desktop-navigation')
    create_upload_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-create-upload-link")]')
    create_live_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-create-live-link")]')
    create_group_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-create-group-link")]')
    create_channel_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-create-channel-link")]')
    create_record_or_video_link = (By.XPATH, '//a[contains(@data-bi-id, "topbar-create-record-screen-link")]')
    search_button = (By.XPATH, '//button[contains(@class, "topbar-search-button")]')
    search_input = (By.XPATH, '//button[contains(@class, "search-input")]')
    upload_button = (By.XPATH, '//a[contains(@data-bi-id, "topbar-upload-button")]')
    invite_button = (By.XPATH, '//a[contains(@data-bi-id, "topbar-invite-button")]')
    feedback_button = (By.XPATH, '//a[contains(@aria-label, "sendfeedback")]')
