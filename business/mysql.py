import common.mysqlClient as mysqlClient
from config.mysqlConfig import dbList
#mr查询
def getMr(f_id,env1=None,symbol=None):
    mrDB=dbList[env1]['ex1']
    sql1 = 'select concat(f_id,"|",symbol),contract_code,order_type,role,mr  from '+mrDB+'.t_exchange_match_result a where  f_id =' + str(f_id)+' and (symbol="'+symbol+'" or contract_code="'+symbol+'");'
    mr = str(mysqlClient.mysql(env1).mysql(sql1))
    mr=mr.replace('\',\'','\'%\'').split('%')
    if mr=='()':return False
    else:return mr
