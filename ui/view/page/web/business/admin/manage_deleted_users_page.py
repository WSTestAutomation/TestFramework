from selenium.webdriver.common.by import By

class ManageDeletedUserPage:
    setting_button = (By.XPATH, '//span[@class="ms-Icon--Settings"]')
    adminsettings_link = (By.PARTIAL_LINK_TEXT, 'Admin')
    data_privacy = (By.XPATH, '//button[@class="c-glyph" and @aria-controls="manage-users-navigation"]')
    manage_deleted_users = (By.XPATH, '//button[text()=" Manage deleted users "]')
    search_delete_users = (By.XPATH, '//input[@id="search-e7a33b07-a97e-0319-10bc-94aca0f236c2"]')
    search_button = (By.XPATH, '//button[@class="c-glyph search-button"]')

    


