import os
import sys
import yaml
from common.lib.base_log import Log
from common.lib.base_config import API_CONFIG_DIR, API_DATABASE_DIR, API_OUTPUT_DIR
from selenium.webdriver import DesiredCapabilities

api_log_dir = os.path.join(API_OUTPUT_DIR, 'logs')
Logger = Log(api_log_dir).get_logger() # 初始化日志模块，后续用Logger或直接用logging都可以。