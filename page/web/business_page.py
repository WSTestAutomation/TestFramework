# coding=utf-8
# @Time    :
# @Author  :
# @File    : business_page.py

from selenium.webdriver.common.by import By


class BusinessPage:
    submit_button = (By.ID, 'submit2')
    add_info_button = (By.CSS_SELECTOR, 'input[value="新  增"]')
    close_button = (By.CSS_SELECTOR, 'input[value="关  闭"]')
    query_button = (By.CSS_SELECTOR, 'input[value="查  询"]')
    apply_button = (By.CSS_SELECTOR, 'input[value="申  请"]')
    enter_button = (By.CSS_SELECTOR, 'input[value="进  入"]')
    back_button = (By.CSS_SELECTOR, 'input[value="返  回"]')
    confirm_button = (By.CSS_SELECTOR, 'input[value="保  存"]')

    # iframe
    iframe_id = 'fraInterface'

    # select options
    code_select = (By.ID, 'codeselect')

    # feedback
    feedback_common = (By.ID, 'contentTD')
    feedback_submit_button = (By.ID, 'butSubmit')

    # window name
    system_info_window_name = '提示'
    
    # 附件上传
    upload_path = (By.ID, 'UploadPath')
    upload_button = (By.ID, 'UploadButton')
