import pyautogui
import os


def upload_by_keys(file):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    test_data_path = os.path.join(base_dir, 'test_data')
    filename = '{}{}{}'.format(test_data_path, os.sep, file)
    pyautogui.sleep(1)
    pyautogui.typewrite(filename, interval=0.5)
    pyautogui.press('enter', interval=0.5)
