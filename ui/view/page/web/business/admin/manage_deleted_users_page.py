from selenium.webdriver.common.by import By

class ManageDeletedUserPage:
    setting_button = (By.XPATH, '//span[@class="ms-Icon--Settings"]')
    adminsettings_link = (By.PARTIAL_LINK_TEXT, 'Admin')
    data_privacy = (By.XPATH, '//button[@class="c-glyph" and @aria-controls="manage-users-navigation"]')
    manage_deleted_users = (By.XPATH, '//button[text()=" Manage deleted users "]')
    search_delete_users = (By.CSS_SELECTOR, 'input#search-f0a37c1a-9a5b-148b-c332-ba26f942fc84')
    search_button = (By.XPATH, '//button[@class="c-glyph search-button"]')

    


