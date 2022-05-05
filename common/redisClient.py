import redis as pyredis,json
from config.redisConfig import redisConf
import allure
import pytest

class redis:
    # global Server1
    def __init__(self,Server, product=None):
        global server
        server=Server
        self.redisServer = redisConf[Server][product]
        self.redis_ip = self.redisServer[0];
        self.port = self.redisServer[1];
        self.redis_password = self.redisServer[2]
    # def redisConfigs(Server, product=None):
    #     return redisConf[Server][product]
    def a(self):pass
    def redis(self,type1,keyname,key=0,value=0,value2=1,log_level=None,port=None):
        # redisServer=redisConfigs(server,product)
        # if port: port=[port]
        # if not port: port = redis_port
        # redis_ip=redisServer[0];port=redisServer[1];redis_password=redisServer[2]
        # print(server)
        if type(self.port)==list:
            for i in range(len(self.port)):
                #打印 环境、参数、服务器地址 端口
                if log_level==1: print('test'+server+' ',type1,keyname,key,value,'redis_server:',self.redis_ip,self.port[i])
                #连接redis
                pool = pyredis.ConnectionPool(host= self.redis_ip, port= self.port[i], password= self.redis_password)
                r = pyredis.Redis(connection_pool=pool)
                #操作类型
                if type1 == "get" :            result = r.get(keyname)
                if type1 == "hget":            result = r.hget(keyname,key)
                if type1 == "hgetall":         result = r.hgetall(keyname)
                if type1 == "hset":            result = r.hset(keyname,key,value)
                if type1 == "lrange":          result = r.lrange(keyname, key, value)
                if type1 == "lset":             result = r.lset(keyname, key, value)
                if type1 == "rpush":          result = r.rpush(keyname, key)
                if type1 == "set":             result = r.set(keyname,value)
                if type1 == "delete":         result = r.delete(keyname)
                if type1 == "keys":           result = r.keys(keyname)
                # print(i,result)
                if str(result)!='None' and str(result)!='{}' and str(result)!='[]':
                    if type1 not in ['keys']:
                        return json.loads(str(result)[2:-1])
                    else:return result
    def init(self,ret):
        if str(ret) == 'None':return "None"
        else:    return ret.decode()