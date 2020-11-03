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
    home_link = (By.XPATH, '//li[contains(@class, "home-menu-ite")]')
    discover_button = (By.ID, 'topbar-discover-navigation-button-desktop')
    discover_video_link = (By.PARTIAL_LINK_TEXT, 'Video')
    discover_channel_link = (By.PARTIAL_LINK_TEXT, 'Channel')
    discover_people_link = (By.PARTIAL_LINK_TEXT, 'People')
    discover_group_link = (By.PARTIAL_LINK_TEXT, 'Group')
    myContent_button = (By.ID, 'topbar-mycontent-navigation-button-desktop')
    myContent_videos_link = (By.PARTIAL_LINK_TEXT, 'Videos')
    myContent_groups_link = (By.PARTIAL_LINK_TEXT, 'Groups')
    myContent_channels_link = (By.PARTIAL_LINK_TEXT, 'Channels')
    myContent_meetings_link = (By.PARTIAL_LINK_TEXT, 'Meetings')
    myContent_watchlist_link = (By.PARTIAL_LINK_TEXT, 'Watchlist')
    myContent_followed_channels_link = (By.PARTIAL_LINK_TEXT, 'Followed Channels')
    myContent_recycle_bin_link = (By.PARTIAL_LINK_TEXT, 'Recycle Bin')
    create_button = (By.ID, 'create-desktop-navigation')
    create_upload_link = (By.PARTIAL_LINK_TEXT, 'Upload')
    create_live_link = (By.PARTIAL_LINK_TEXT, 'Live')
    create_group_link = (By.PARTIAL_LINK_TEXT, 'Group')
    create_channel_link = (By.PARTIAL_LINK_TEXT, 'Channel')
    create_record_or_video_link = (By.PARTIAL_LINK_TEXT, 'Record or Video')
    search_button = (By.XPATH, '//button[contains(@class, "topbar-search-button")]')
    search_input = (By.XPATH, '//button[contains(@class, "search-input")]')
    upload_button = (By.XPATH, '//a[contains(@data-bi-id, "topbar-upload-button")]')
    invite_button = (By.XPATH, '//a[contains(@data-bi-id, "topbar-invite-button")]')
    feedback_button = (By.XPATH, '//a[contains(@aria-label, "sendfeedback")]')