from config.apiConfig import apiUrls,api_path
from config.keyConfig import KEY
from common.util import printc
import common.util as u,datetime
import config.commonConfig as conf,json
class api:
    def __init__(self,server,product=None,user_id=None):
        if not user_id: user_id=conf.defaultUser_id[server[:-1]]
        self._server=server;self._userId = user_id;
        self.ACCESS_KEY=KEY[server[:-1]][user_id][0];self.SECRET_KEY=KEY[server[:-1]][user_id][1];
        self.apiUrl=apiUrls[server[:-1]][server[-1:]]+api_path[server[-1:]]
        # print(self.apiUrl,self.ACCESS_KEY,self.SECRET_KEY)
    def send_order(self,contract_code,price,volume=1,direction='buy',offset='open',lever_rate=5,order_price_type='limit',pair=None,mode_type=None,contract_type=None,client_order_id=None,log_level=None):
        params = {"price": price,"volume": volume,"direction": direction,"offset": offset,
                  "lever_rate": lever_rate,"userId":self._userId,  #lever_rate支持蛇形(lever_rate)、驼峰结构(leverRate)
                  "order_price_type": order_price_type,"contract_type": "swap","pair":"BTC-USDT"}
        if self._server[-1:] == conf.linear_flag:
            params['reduce_only']=0
            contract_info=self.contract_info(contract_code)
            contract_code=contract_info['data'][0]['contract_code']
            if str(contract_code).count('-')==2:
                mode_type=True #正向交割 仅支持全仓
                contract_type=contract_info['data'][0]['contract_type']
                pair=contract_info['data'][0]['pair']
        if contract_code:       params['contract_code'] = contract_code
        client_order_id=str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','').replace('.','')[:17]
        if client_order_id:     params['client_order_id'] = client_order_id
        if  pair: params['pair'] = pair
        if contract_type:     params['contract_type'] = contract_type
        request_path = 'swap_order';cross_flag = conf.isolateName
        if mode_type: request_path='swap_cross_order';cross_flag = conf.crossName
        if log_level in [1,3]: print('正向永续' + cross_flag + '-下单请求参数:', self.apiUrl + request_path,'\n', json.dumps(params))
        return u.apiKeyPost(self.apiUrl, request_path, params, self.ACCESS_KEY, self.SECRET_KEY)
    def contract_info(self,contract_code=None,contract_type=None,symbol=None,pair=None,log_level=None):
        params={}
        if contract_code: params['contract_code'] = contract_code
        if self._server[-1:]==conf.linear_flag:
            params['business_type']='all';params['partition']='all';
            if str(contract_code).count('-')==2 and '2' not in str(contract_code): #正向交割,兼容BTC-USDT-CW格式
                contract_type1=conf.futureType[contract_code[-2:].upper()]
                params['contract_type']=contract_type1
                params['pair'] = contract_code[:-3];params.pop('contract_code')
        if symbol:params['symbol'] = symbol
        if contract_type:   params['contract_type'] = contract_type

        request_path = 'swap_contract_info'
        if log_level in [1,3]: print('正向永续-查询合约信息：', self.apiUrl + request_path, params)
        r=u.request_http('get',self.apiUrl+request_path, params)
        if r['status']=='ok': return r
        else:printc('contract_info API 查询失败',r);return False
