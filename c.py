from config.apiConfig import apiUrls,api_path
from config.orderConfig import orderUrls,orderPath,orderPath2
from business.order.order import order
from business.api.api import api
from common.util import printc,request_http,truncate
import sys,json
class c:
    def __init__(self, server, access_key=None, secret_key=None):
        # print(apiUrls[server[:-1]][server[-1:]])
        self._server=server
        self.apiUrl=apiUrls[server[:-1]][server[-1:]]+api_path[server[-1:]]
        self.orderUrl = orderUrls[server[:-1]] + orderPath[server[-1:]]+orderPath2[server[-1:]]
    def probe(self):
        _order = order(self._server);_api=api(self._server)
        order_contractInfo = _order.contract_info();api_contractInfo=_api.contract_info()
        if api_contractInfo['status'] != 'ok': printc('api contractInfo Error：', api_contractInfo)
        if order_contractInfo['status']!='ok': printc('order contractInfo Error：',order_contractInfo)
        turnover = request_http('get','https://testdm.huobi.be/contract-center-order/x/v1/center_current_trade_turnover','', log_level=0);
        turnover_number = turnover['data'].__len__()
        if turnover_number < 3: printc('成交额业务线<3.请联系开发人员排查', turnover);
        else:print('futuresTradeTurnoverAll = ', int(truncate(turnover['data'][0]['trade_turnover'] + turnover['data'][1]['trade_turnover'] +turnover['data'][2]['trade_turnover'], 0)) / 10000,'W')

c('20l').probe()
if sys.argv.__len__()>1:
    option=sys.argv[1];server=sys.argv[2]
    #探针检查
    if option=='probe': c(server).probe()