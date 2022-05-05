import pytest, allure,os
from common.noti_restful import t
from common.util import compare
from config.notiConfig import contract_code,all_period
# @allure.epic('epic')
# @allure.feature('feature')
# @allure.story('story')
@allure.tag('Script owner : brian', 'Case owner : brian')
@pytest.mark.noti
class TestCase_3():
    # titlename = 'restful请求kline,传size'
    # @allure.title(titlename)
    def test_2(self):
        os.system('rm -rf /Users/jilong/py3/report/allure/*')
        assert 'h' in "hello"
    def test_3(self):
        assert 'h' in "hello"

    @allure.title('restful请求kline,传from,to')
    def test_4(self):
        # assert 'h' in "hello"
        with allure.step('restful请求kline,传from,to'):
            r=t.kline('btc-usdt','15min',FROM=1651111200,to=1651125600,log_level=0)
            contract_code = 'btc-usdt';period ='15min';size = 3
            schema = {'ch': f'market.{contract_code.upper()}.kline.{period}', 'ts': int, 'status': 'ok', 'data': [{'id': float}]}
            compare_r = compare(schema, r, title=['<Kline restful 传from to> [basic check] ', contract_code, period, size])
            if not compare_r:   assert False,'验证不通过'
            else: assert  True,'验证通过'
            pass

    @allure.title('restful请求kline,传size')
    def test_excute(self, ):
        with allure.step('restful请求kline,传size'):
            r1=[]
            for i in all_period:
                # contract_code='btc-usdt';
                period=i;size=3
                r=t.kline(contract_code,i,3,log_level=0)
                schema = {'ch': f'market.{contract_code.upper()}.kline.{period}','ts':int,'status':'ok','data':[{'id':int}]}
                compare_r=compare(schema,r,title=['<Kline restful 传size> [basic check] ',contract_code,period,size])
                r1.append(compare_r)
            # print(r1)
            if not compare_r:   assert False,'验证不通过'
            else: assert  True,'验证通过'
                # pass
# if __name__ == '__main__':
#     pytest.main()