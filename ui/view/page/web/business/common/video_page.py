# coding=utf-8
# @Time    :
# @Author  :
# @File    : video_page.py

from selenium.webdriver.common.by import By

class VideoPage:
    video_statistics_like = (By.XPATH, '//span[contains(@class, "like-count")]/span')
    like_button = (By.CLASS_NAME, 'video-like')
