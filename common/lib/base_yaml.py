# coding=utf-8

import os
import yaml
from common.lib.base_config import UI_CONFIG_DIR


class Yaml:

    def __init__(self, file_path):
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            raise FileNotFoundError('file does not exist')
        self._data = None

    def read(self):
        if not self._data:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self._data = yaml.safe_load(file)
                file.close()
            return self._data

    def read_get(self, key):
        return self.read()[key]

    def write(self, data):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                yaml.dump(data, file, allow_unicode=True, default_flow_style=False)
                file.close()
        except Exception:
            raise Exception('Failed to write yaml file')

    # 二进制读取数据
    def data(self):
        if not self._data:
            with open(self.file_path, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
            return self._data

    def data_get(self, element, index=0):
        return self.data()[index].get(element)


if __name__ == '__main__':
    yaml_file = os.path.join(UI_CONFIG_DIR, 'web_config.yaml')
    y = Yaml(yaml_file)
    y.read_get('env')
