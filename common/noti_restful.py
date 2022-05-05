import json

from config.urlConfig import url;#from config.urlConfig import noti_path
from config.notiConfig import noti_path
from common.util import request_http,printc
import config.urlConfig as urlconf
import config.commonConfig as conf
def compare(schema,r,title=None):
    compareResult=True;title_print=title[0]+title[1]+' '+title[2]+' '
    for i in schema.keys():
        if i in r:
            if type(schema[i]) == str:   #预期结果为字符串则直接对比，不符合预期则抛出
                if not r[i] == schema[i]:     printc(title_print,i,'=',r[i],' 预期:',schema[i],' 实际:',r[i]);compareResult=False
            if type(schema[i]) == type:  #预期结果为数据类型则用类型对比，不符合预期则抛出
                if not type(r[i]) == schema[i]: printc(title_print,i,'=',r[i],' 预期:',schema[i],' 实际:',type(r[i]));compareResult=False
            if type(schema[i]) == dict:          #预期结果为字典
                compare(schema[i],r[i],title=title)

            if type(schema[i]) == list:     #预期结果为数组
                # print(title)
                for k in range(r[i].__len__()):      #实际的数据可能存在多个数组需要遍历
                    if type(schema[i]) == list:
                        for j in range(schema[i].__len__()):     #每个基础数组中对应的数据
                            if type(schema[i][j])==list:
                                if schema[i][j].count(type(r[i][k][j]))>0:pass         #预期类型为多个类型
                                else: printc(title_print,k+1,schema[i][j],r[i][k][j]); compareResult=False;#exit()
                            elif type(schema[i][j])==dict: compareResult=compare(schema[i][j],r[i][k],title=title);    #           #预期类型为字典
                            else:
                                # print(schema[i][j],r[i][k],j)
                                if schema[i][j]==type(r[i][k][j]):pass               #预期类型为单个类型
                                else: printc(title_print,k+1,schema[i][j],r[i][k][j]); compareResult=False;
                        if not compareResult:break
                            # if type(r[i][0][j]) in schema[i][j]:pass
                            # else:print(2,schema[i],schema[i][j],r[i][0])
                    elif  type(schema[i]) == dict:  print(1111)#compare(schema[i],r[i])
        else:
            printc(title_print,'Key不存在',i,'实际:',r,p_type='green');compareResult=False;
    return compareResult

class restful():
    def __init__(self,server):
        global this_server,contract_code_type,schema
        self.noti_url = url[server]['noti']
        self.noti_path=noti_path[server[-1:]]
        self.notiUrl=self.noti_url+self.noti_path  #获取noti restful公用url路径
        this_server=server;contract_code_type=conf.contract_code_type_SwapLinear
        if this_server[-1:] == conf.contract_flag:contract_code_type=conf.contract_code_type_Contract #交割用"symbol"

    def depth(self,contract_code=None,type1=None,log_level=None):
        params = {contract_code_type: contract_code,'type': type1};url = self.notiUrl + '/market/depth'
        r=request_http('get', url, params, log_level=log_level)
        schema = {'ch': f'market.{contract_code.upper()}.depth.step0','status': 'ok','tick':{"asks":[[float,int],int],"bids":[[float,int],int]},'ts':str}
        return compare(schema,r,title=['<Depth restful> [basic check] ',contract_code,type1])

    def kline(self, contract_code=None, period=None, size=None, FROM=None, to=None,log_level=None,flag=None):
        params = {'contract_code': contract_code,'period': period}
        if FROM:   params['from'] = FROM
        if to:   params['to'] = to
        if size:   params['size'] = size
        url = self.notiUrl + '/market/history/kline'
        r=request_http('get', url, params, log_level=log_level)
        if flag:
            schema = {'ch': f'market.{contract_code.upper()}.kline.{period}','ts':int,'status':'ok','data':[{'id':float}]}
            return compare(schema,r,title=[flag,contract_code,period,size])
        return r
t=restful('20l')
# t=restful('20l').depth('btc-usdt','step0',log_level=0)
