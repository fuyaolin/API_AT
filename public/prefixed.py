"""
    读取前置后置文件
    然后执行脚本
"""
import os
import sys
from common.log import Logger
from common.read_path import SETUP_PATH, TEARDOWN_PATH


class Prefixed(object):
    def __init__(self, prefixed_value):
        self.SETUP_PATH = SETUP_PATH
        self.TEARDOWN_PATH = TEARDOWN_PATH
        self.prefixed_file = prefixed_value.split(".")[0]
        self.prefixed_function = prefixed_value.split(".")[-1]

    def execute(self, file_path):
        if os.path.exists(file_path):
            for root, dirs, files in os.walk(file_path):
                dirs = 'setup' if root.split(os.path.sep)[-1] == 'setup' else 'teardown'
                if str(self.prefixed_file+".py") in files:
                    import_exe = 'from public.{dirs}.{files} import {function}'.\
                        format(dirs=dirs, files=self.prefixed_file, function=self.prefixed_function)
                    exec(import_exe)
                    break
        else:
            Logger().logs_file().info("前置路径不存在：" + str(file_path))

    def exe_prefixed(self):
        sys.path.append(self.SETUP_PATH)
        self.execute(self.SETUP_PATH)

    def exe_suffixed(self):
        sys.path.append(self.TEARDOWN_PATH)
        self.execute(self.TEARDOWN_PATH)


if __name__ == '__main__':
    Prefixed("setup_file.setup_function").exe_prefixed()
