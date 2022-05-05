import common.noti_ws as ws;
from common.util import subs
import common.util as u,time,websockets,json,gzip,asyncio,traceback
from config.notiConfig import ws_urls,ws_path
import sys
class wsForver:
    def __init__(self, server, access_key=None, secret_key=None):
        self.__url=ws_urls[server[:-1]]+ws_path[server[-1:]]
    def suball(self,contract_code,period):
        wsMsg= [{"sub": "market.{}.kline.{}".format(contract_code, period),"id": "sub_kline"},{"sub": "market.{}.bbo".format(contract_code),"id": "sub_bbo"}]
        # wsMsg = {"sub": "market.{}.bbo".format(contract_code),"id": "id-bbo"}
        subs(self.__url, wsMsg, 'tick')
    def req_kline(self,contract_code,period,from_=None,to_=None):
        to_=int(time.time())
        if period in ['1min']:from_=u.timeToStamp(u.timePlus(-30,period='minute'));
        wsMsg = {"req": "market.{}.kline.{}".format(contract_code, period), "from": int(from_), "to": int(to_)};subs(self.__url, wsMsg,topic='req_kline')
async def subscribe(url, subs, callback=None, ):
    async with websockets.connect(url) as websocket:
        for sub in subs:
            sub_str = json.dumps(sub)
            await websocket.send(sub_str)
            # print(f"send: {sub_str}")
        for i in range(1):
            rsp = await websocket.recv()
            data = json.loads(gzip.decompress(rsp).decode())
            if  "ping" in data:
                pong_msg = {"pong": data.get("ping")}
                await websocket.send(json.dumps(pong_msg))
                continue
            if "newtest20" in url:tag = 'old'
            else:   tag = 'new'
            if 'tick' in str(data):
                rsp = await callback('{}'.format(tag), data)
            # print(res2)
async def handle_ws_data(*args, **kwargs):
    """ callback function
    Args:
        args: values
        kwargs: key-values.
    """
    # if args[0]=='old': r[0]=args[1]
    # if args[0] == 'new': r[1] = args[1]
    # print(r[0])
    print(*args,**kwargs)
async def multiple_tasks(url1, url2, subs):
    input_coroutines = [subscribe(url1, subs, handle_ws_data), subscribe(url2, subs, handle_ws_data)]
    res = await asyncio.gather(*input_coroutines, return_exceptions=True)
    return res
def run(url1, url2 ,subs):
    # while True:
    for i in range(3):
        try:
            asyncio.get_event_loop().run_until_complete(multiple_tasks(url1, url2 ,subs))
        except Exception as e:
            traceback.print_exc()
            print('websocket connection error. reconnect rightnow')
class wsDouble:
    def __init__(self, server, access_key=None, secret_key=None):
        self.__url=ws_urls[server[:-1]]+ws_path[server[-1:]]
    def subDouble(self,contract_code,period):
        url1 = "ws://newtest20-contract-hw.dm.huobiapps.com/linear-swap-ws"
        url2 = "ws://test-20.dm.huobiapps.com/linear-swap-ws"
        market_subs = [{
            #  K线
            "sub": "market.{}.kline.{}".format(contract_code.upper(), period),
            "id": 'test_kline_sub'}]
        run(url1,url2,market_subs)
                    # rsp = await callback('{}'.format(tag), data)  # 修改data内容改变格式
# wsForver('20l').req_kline('btc-usdt-cw','1min')
wsDouble('20l').subDouble('btc-usdt','1min')