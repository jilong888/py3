import pytest, allure
from common.noti_restful import t
# @allure.epic('epic')
# @allure.feature('feature')
# @allure.story('story')
@allure.tag('Script owner : brian', 'Case owner : brian')
@pytest.mark.noti
class Test_Noti_Depth:
    titlename = 'restful请求depth'
    @allure.title(titlename)
    def test_execute(self, ):
        with allure.step('restful请求depth'):
            r=t.depth('btc-usdt','step0',log_level=0)
            if not r:   assert False,'验证不通过'
            else: assert  True,'验证通过'
            pass
# if __name__ == '__main__':
#     pytest.main()