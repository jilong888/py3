#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2022/4/19 11:35 上午
# @Author  : HuiQing Yu

import pytest, allure



@allure.epic('epic')
@allure.feature('feature')
@allure.story('story')
@allure.tag('Script owner : 余辉青', 'Case owner : ')
@pytest.mark.stable2
class TestAbc_01:
    titlename='正向永续订阅成交'

    @allure.title(titlename)
    def test_execute(self,):
        fail_reason = 'it is fail';
        with allure.step('操作:执行请求'):
            assert True,'验证通过'
            pass
        with allure.step('验证第二步:'):
            a=1
            if a:
                assert True,'验证通过'
                pass
            else:
                assert False, '验证不通过\t\n' + fail_reason+'\t\n abc'