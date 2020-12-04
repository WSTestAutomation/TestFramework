from selenium.webdriver.common.by import By

class ManageDeletedUserPage:
    setting_button = (By.XPATH, '//span[@class="ms-Icon--Settings"]')
    adminsettings_link = (By.PARTIAL_LINK_TEXT, 'Admin')
    data_privacy = (By.XPATH, '//button[@class="c-glyph" and @aria-controls="manage-users-navigation"]')
    manage_deleted_users = (By.XPATH, '//button[text()=" Manage deleted users "]')
    search_delete_users = (By.XPATH, '//input[starts-with(@id,"search")]')
    search_button = (By.XPATH, '//button[@class="c-glyph search-button"]')

    edit_button = (By.XPATH, '//button[@class="edit c-action-trigger"]//*[name()="svg"]/*[name()="use"]')
    delete_button = (By.XPATH, '//button[@class="delete c-action-trigger"]//*[name()="svg"]/*[name()="use"]')
    cancel_delete_button = (By.XPATH, '//button[@class="stream-btn dialog-cancel-button ng-binding ng-scope"]')
    # Edit user details
    edit_name = (By.XPATH, '//input[starts-with(@class,"ct-textbox-compact")]')
    save_edit_button = (By.XPATH, '//button[@class="stream-btn right-dialog-button ng-binding btn-primary"]')
    cancel_edit_button = (By.XPATH, '//button[@class="stream-btn left-dialog-button ng-binding"]')



    


