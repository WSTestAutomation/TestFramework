from selenium.webdriver.common.by import By

class ManageDeletedUserPage:
    manage_deleted_users = (By.XPATH, '//button[text()=" Manage deleted users "]')
    manage_deleted_users_model = (By.XPATH, '//div[@class="forgotten-users-settings"]')
    search_delete_users = (By.XPATH, '//input[starts-with(@id,"search")]')

    # 成功找到的用户
    exist_user = (By.XPATH, '//header[@ng-transclude="header"]')

    edit_button = (By.XPATH, '//button[@class="edit c-action-trigger"]//*[name()="svg"]/*[name()="use"]')
    delete_button = (By.XPATH, '//button[@class="delete c-action-trigger"]//*[name()="svg"]/*[name()="use"]')
    cancel_delete_button = (By.XPATH, '//button[@class="stream-btn dialog-cancel-button ng-binding ng-scope"]')

    # Edit user details
    edit_name = (By.XPATH, '//input[starts-with(@class,"ct-textbox-compact")]')
    save_button = (By.XPATH, '//button[@class="stream-btn right-dialog-button ng-binding btn-primary"]')
    cancel_edit_button = (By.XPATH, '//button[@class="stream-btn left-dialog-button ng-binding"]')
