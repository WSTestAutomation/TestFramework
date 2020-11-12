# coding=utf-8

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

UI_DIR = os.path.join(BASE_DIR, 'ui')
UI_CONFIG_DIR = os.path.join(UI_DIR, 'config')
UI_DATABASE_DIR = os.path.join(UI_DIR, 'database')
UI_OUTPUT_DIR = os.path.join(UI_DIR, 'output')
UI_DRIVERS_DIR = os.path.join(UI_DIR, 'drivers')
UI_TEST_DIR = os.path.join(UI_DIR, 'test')

API_DIR = os.path.join(BASE_DIR, 'api')
API_CONFIG_DIR = os.path.join(API_DIR, 'config')
API_DATABASE_DIR = os.path.join(API_DIR, 'database')
API_OUTPUT_DIR = os.path.join(API_DIR, 'output')
API_TEST_DIR = os.path.join(API_DIR, 'test')
