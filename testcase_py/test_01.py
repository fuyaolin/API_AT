# -*- coding: utf-8 -*-
import pytest
from common.Data_Manager import Runcase
from common.Read_Path import TESTCASE_YAML_NAME_PATH

PATH = TESTCASE_YAML_NAME_PATH
CASE = Runcase().case(PATH)
skip_reason = PATH + "(testcase skip)"


# @allure.story('')
class Test_01(object):
    @pytest.mark.skipif(len(CASE) == 0, reason=skip_reason)
    # @allure.story('')
    @pytest.mark.parametrize('case', CASE)
    def test_01(self, case):
        Runcase().all_run(path=PATH, case=case)


if __name__ == '__main__':
    pytest.main(['-v','test_01.py'])
