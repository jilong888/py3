from common.util import sub, api_key_sub
from config.notiConfig import noti_path,ws_path,ws_urls
# from config.conf import WSURL, ACCESS_KEY, SECRET_KEY

class WebsocketSevice:
    def __init__(self, server, access_key, secret_key):
        self.__url=ws_urls[server[:-1]]+ws_path[server[-1:]]
        # self.__url = url+ws_path['linear']
        self.__access_key = access_key
        self.__secret_key = secret_key

    def sub_bbo(self, contract_code):
        subs = {"sub": "market.{}.bbo".format(contract_code),"id": "id-bbo"}; return sub(self.__url, subs, 'tick')

    def sub_kline(self, contract_code, period):
        subs = {"sub": "market.{}.kline.{}".format(contract_code, period),"id": "id1"}; return sub(self.__url, subs, 'tick')

    def req_kline(self, contract_code, period, from_, to):
        subs = { "req": "market.{}.kline.{}".format(contract_code, period), "from": int(from_),"to": int(to)};  return sub(self.__url, subs)

    def sub_depth_web(self,contract_code,type):
        subs = {"sub": "market.{}.depth.{}.sync".format(contract_code, type),"id": "id_depth_web"};  return sub(self.__url, subs,'tick')

    def sub_depth_high_freq(self, contract_code, size, data_type="incremental"):
        subs = {"data_type": data_type,"sub": "market.{}.depth.size_{}.high_freq".format(contract_code, size),"id": "id1"};  return sub(self.__url, subs,'tick')

    def sub_detail(self, contract_code):
        subs = {"sub": "market.{}.detail".format(contract_code),"id": "id_detail"};  return sub(self.__url, subs)

    def sub_trade_detail(self, contract_code):
        subs = { "sub": "market.{}.trade.detail".format(contract_code),"id": "id_trade_detail"};  return sub(self.__url, subs,'tick')
    def req_trade_detail(self, contract_code, size=None):
        subs = {"req": "market.{}.trade.detail".format(contract_code),"id": "id_req_trade_detail"}
        if size:    subs['size'] = size
        return sub(self.__url, subs, 'data',p_flag=0)
    # 订阅聚合行情
    def sub_detail_merged(self, contract_code):
        subs = {"zip": 0,"sub": f"market.{contract_code}.detail","id": "id_sub_detail_merged"};  return sub(self.__url, subs)
    # 订阅深度图
    def sub_depth_chart(self, contract_code, percent='percent10'):
        subs = {"sub": f"market.{contract_code}.depth.{percent}","id": "id8"};  return sub(self.__url, subs)

    def sub_account(self, contract_code):
        subs = {"op": "sub", "cid": '11433583', "topic": "accounts.{}".format(contract_code)}
        path = '/linear-swap-notification'
        url = self.__url
        url='ws://test-20.dm.huobiapps.com/'
        return api_key_sub(url, self.__access_key, self.__secret_key, subs, path)

# WSURL='ws://test-20.dm.huobiapps.com'
t = WebsocketSevice('20l', '1', '1')