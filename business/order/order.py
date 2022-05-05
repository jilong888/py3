import sys

from config.urlConfig import orderUrls
import config.commonConfig as conf
from config.orderConfig import orderPath,orderPath2
from common.util import request_http,printc
class order:
    global contract_code_date, contract_code_short
    def __init__(self,server,product=None):
        self._server=server
        self.orderUrl=orderUrls[server[:-1]]+orderPath[server[-1:]]+orderPath2[server[-1:]]
    def contract_info(self,contract_code=None):
        if self._server[-1:] == conf.contract_flag: orderName='contract_contract_info'
        else:orderName='contract_info'
        if self._server[-1:]==conf.linear_flag: param={'business_type':'all','trade_partition':'ALL'}
        else:param=''
        r=request_http('get', self.orderUrl+orderName,param, log_level=0)
        if not contract_code: return r
        if r['status']=='ok':
           for i in r['data']:
               if i['contract_code'] == contract_code.upper() or i['contract_short_type'] == contract_code.upper():
                    this_contract_info=i['symbol'],i['contract_code'],i['contract_size'],i['price_tick'],i['contract_status'],i['contract_short_type']
                    self.contract_code_date = this_contract_info[1]
                    self.contract_code_short = this_contract_info[5]
                    return this_contract_info
        else:printc('contract_info查询失败: ',r);sys.exit();
    # def a1(self):
    #     print(self.contract_code_date)
# contract_info=order('20l').contract_info('btc-usdt-cq')
# print(contract_code_date)