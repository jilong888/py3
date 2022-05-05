import config.commonConfig as conf
contract_code='btc-usdt'
all_period=['1min','5min','15min','30min','60min','4hour','1day','1week','1mon']
# schema = {'ch': f'market.{contract_code.upper()}.kline.{}','ts':int,'status':'ok','data':[{'id':int}]}
noti_swap_path='/swap-ex';noti_linear_path='/linear-swap-ex';noti_contract_path='';
noti_path={"s":noti_swap_path,"l":noti_linear_path,"c":noti_contract_path}
swap_ws_path='/swap-ws';linear_ws_path='/linear-swap-ws';contract_ws_path='/ws';
ws_path={conf.swap_flag:swap_ws_path,conf.linear_flag:linear_ws_path,conf.contract_flag:contract_ws_path}
ws_test20_url='ws://test-20.dm.huobiapps.com'
ws_urls={
    '20':ws_test20_url
}
