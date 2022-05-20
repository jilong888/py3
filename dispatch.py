import common.noti_restful as noti;import datetime,time,common.util as u
from common.noti_ws import t as ws;from common.redisClient import redis;from common.rabbitMqClient import rabbitMQ
from common.excel import t as excel
from config.notiConfig import contract_code,all_period
from business.mysql import getMr,mysqlClient
from business.order.order import order
from business.api.api import api
import business.futures.basic as basic

restful_flag=0;ws_flag=0;excel_flag=0;redis_flag=1;mysql_flag=0;mq_flag=0;order_flag=1;api_flag=1;
if restful_flag:
    for period in all_period:
        t=noti.restful('20l').kline('btc-usdt-CW',period,3,log_level=0,flag='<Kline restful 传size> [basic check] ')
if ws_flag:  #WS相关topic订阅
    bbo=ws.linear_sub_bbo('btc-usdt')
    kline=ws.linear_sub_kline('btc-usdt','1min')
    kline=ws.linear_req_kline('btc-usdt','1min',1650769200,1650787200)
    depth=ws.sub_depth_web('btc-usdt-cw','step8')
    freq=ws.sub_depth_high_freq('btc-usdt-cw',150)
    detail=ws.sub_detail('btc-usdt-cw')
    trade_detail=ws.sub_trade_detail('btc-usdt-cw')
    req_trade_detail=ws.req_trade_detail('btc-usdt-cw',3)
    sub_detail_merged=ws.sub_detail_merged('btc-usdt-cw')
    sub_depth_chart=ws.sub_depth_chart('btc-usdt-cw')
    sub_account=ws.sub_account('btc-usdt')
    # print(sub_account)
    print(sub_account)
if excel_flag:
    print(excel.read_excel(1,1))
    # excel.add_excel(1, 1, 'hello,excel2!', 'test2.xls')
    # excel.write_excel(1,1,103.23,'excel.xls')
    # excel.write_excel(2,5,200,'excel.xls')
    excel.write_excel(1,6,'20000','/Users/jilong/py/middleware/test.xls') #用xls文件
    excel.write_excel2('A1',12345,'/Users/jilong/py/middleware/test.xlsx')#用xlsx文件
if redis_flag:
    print(redis('20l', None).redis('keys', 'RsO:USER#10000100*', log_level=0))
    print(redis('20l', None).redis('get', 'RsO:USER#1000010042', log_level=0))
if mysql_flag:
    a = getMr(221600000011853, '20l', 'btc-usdt-cw')#调用封装的sql查询方法
    b=mysqlClient.mysql('20l').mysql('select * from linear_contract_trade.t_trade_user where user_id=11433583')#直接调用sql语句
    print(a);print(b.split(',')[2])
    # for i in a: print(i)

print(u.f(2.33434,3));print(u.StampToTime(1651123365))
print(basic.symbols('btc_3'))
if mq_flag:
    t = rabbitMQ('20l').RabbitMQ(mq_exchange='test1', routing_key='abc', mq_value='11111')
if order_flag:
    r=order('20c')
    r1=r.contract_info('btc_cw')
    print(r.contract_code_date,r.contract_code_short,r.orderUrl)
if api_flag:
    r = api('20l').send_order('btc-usdt-cw', 44511.1, log_level=3, mode_type=1)
    # r=api('20l').contract_info('btc-usdt-cw',log_level=3)
    print(r)

print('hello,world')