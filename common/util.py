import base64,datetime,gzip,hashlib,hmac,json,time,urllib.parse,requests,websocket
# from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5
# from Crypto.PublicKey import RSA
# import websocket

def request_http(method,url,params,v_hbsession=None,log_level=0,op=None):
    session1 = '5e0f5041-712f-4258-8201-92a60c23899f';
    session2 = '78bc48ed-e1fc-4671-baca-bf9cf8e54020';
    session3 = '3c576152-98d8-43ef-947f-23869b6a97e4';

    # v_hbsession=random.choice([session1, session2, session3]) #随机选取用户
    if v_hbsession==None: v_hbsession='3a7647b9-e835-43c8-ab34-555c76fe1baf'
    # v_hbsession=config.hbsession
    headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5","Accept-Encoding":"gzip, deflate, br","Cookie":"token=c7ebd817-d668-46eb-a80f-d5de9cd2f866; expire_time=20211029155728",
               "Accept": "application/json, text/plain, */*","Content-Type":"application/json","Connection":"keep-alive","Accept-Language":"zh-CN","source":"web","hbsession":v_hbsession,"token":v_hbsession}
    if op == 'content': headers['Content-Type'] = ''
    if log_level==1: print(url,params)
    if method=='get':
        r = requests.get(url, params=params,headers=headers) #urllib.parse.urlencode(params) 转码
    elif method=='post':
        if type(params)==dict: r = requests.post(url, json=params,headers=headers)
        else: r = requests.post(url, data=params,headers=headers)
    else:
        return '不被接受的方法，只支持get或post'
    if op=='content': return r.content  #特殊需要解压使用的场景
    if r.status_code == 200:    return r.json()
    else:   return r.text

def printc(s=None,s1=None,s2=None,s3=None,s4=None,s5=None,s6=None,s7=None,s8=None,p_type=None):
    if s1 or s1==0: s=str(s)+str(s1)
    if s2 or s2==0: s = s + str(s2)+' '
    if s3 or s3==0: s = s + str(s3)+' '
    if s4 or s4==0: s = s + str(s4)+' '
    if s5 or s5==0: s = s + str(s5)+' '
    if s6 or s6==0: s = s + str(s6)+' '
    if s7 or s7==0: s = s + str(s7)+' '
    if s8 or s8==0: s = s + str(s8)+' '
    if p_type=='green':         print('\033[0;36;2m',s,'\033[0m ');
    elif p_type=='yellow':       print('\033[0;32;2m',s,'\033[0m ');
    else:                        print('\033[0;31;3m',s,'\033[0m ');

def compare(schema, r, title=None):
    compareResult = True;
    title_print = title[0] + title[1] + ' ' + title[2] + ' '
    for i in schema.keys():
        if i in r:
            if type(schema[
                        i]) == str:  # 预期结果为字符串则直接对比，不符合预期则抛出
                if not r[i] == schema[i]:     printc(title_print, i, '=', r[i], ' 预期:', schema[i], ' 实际:',
                                                     r[i]);compareResult = False
            if type(schema[
                        i]) == type:  # 预期结果为数据类型则用类型对比，不符合预期则抛出
                if not type(r[i]) == schema[i]: printc(title_print, i, '=', r[i], ' 预期:', schema[i], ' 实际:',
                                                       type(r[i]));compareResult = False
            if type(schema[
                        i]) == dict:  # 预期结果为字典
                compare(schema[i], r[i], title=title)

            if type(schema[
                        i]) == list:  # 预期结果为数组
                # print(title)
                for k in range(r[
                                   i].__len__()):  # 实际的数据可能存在多个数组需要遍历
                    if type(schema[i]) == list:
                        for j in range(schema[
                                           i].__len__()):  # 每个基础数组中对应的数据
                            if type(schema[i][j]) == list:
                                if schema[i][j].count(type(r[i][k][j])) > 0:
                                    pass  # 预期类型为多个类型
                                else:
                                    printc(title_print, k + 1, schema[i][j], r[i][k][
                                        j]); compareResult = False;  # exit()
                            elif type(schema[i][j]) == dict:
                                compareResult = compare(schema[i][j], r[i][k],
                                                        title=title);  # #预期类型为字典
                            else:
                                # print(schema[i][j],r[i][k],j)
                                if schema[i][j] == type(r[i][k][j]):
                                    pass  # 预期类型为单个类型
                                else:
                                    printc(title_print, k + 1, schema[i][j], r[i][k][j]); compareResult = False;
                        if not compareResult: break
                        # if type(r[i][0][j]) in schema[i][j]:pass
                        # else:print(2,schema[i],schema[i][j],r[i][0])
                    elif type(schema[i]) == dict:
                        print(
                            1111)  # compare(schema[i],r[i])
        else:
            printc(title_print, 'Key不存在', i, '实际:', r, p_type='green');
            compareResult = False;
    return compareResult
def subs(url, wsMsg,keyword=None,p_flag=None,topic=None):
    ws = websocket.create_connection(url)
    # sub_str = json.dumps(wsMsg)
    if type(wsMsg)==list:
        for Msg in wsMsg:
            ws.send(json.dumps(Msg))
    else:ws.send(json.dumps(wsMsg))
    s = 0
    for i in range(9999):
        r = json.loads(gzip.decompress(ws.recv()).decode())
        if  'ping' in r or 'ping' in str(r):
            nowTime = lambda: int(round(time.time() * 1000))
            ts = r['ping']
            ws.send('{"pong":' + str(ts) + '}')
        if 'ping' not in r:
            s=s+1;
            if topic=='req_kline':
                for klineData in r['data']:
                    klineData['id']=StampToTime(klineData['id'])
                    print(klineData)
            else: print(s,r)
def sub(url, subs, keyword=None,p_flag=None):
    try:
        ws = websocket.create_connection(url)
        sub_str = json.dumps(subs)
        if p_flag: print('\33[0;32;49m%s\33[0m' %f'\n\turl={url},{str(subs)}')
        ws.send(sub_str)
        sub_result = json.loads(gzip.decompress(ws.recv()).decode())
        if keyword:
            for i in range(3):
                if keyword in str(sub_result):
                    break
                else:
                    if p_flag: print(f'返回数据中无关键key={keyword},实际结果={sub_result},第{i + 1}次重试……')
                    sub_result = json.loads(gzip.decompress(ws.recv()).decode())

        result_info = '请求结果: \t' + str(sub_result)
        if p_flag : print('\033[1;32;49m%s\033[0m' % result_info)
        ws.close()
        return sub_result
    except Exception as e:
        print("Sub failed, detail is:%s" % e)
        return {"status": "fail", "msg": "%s" % e}
# 鉴权订阅
def api_key_sub(url, access_key, secret_key, subs, path='/notification'):
    host_url = urllib.parse.urlparse(url).hostname.lower()
    print(host_url)
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
    data = {
        "AccessKeyId": access_key,
        "SignatureMethod": "HmacSHA256",
        "SignatureVersion": "2",
        "Accept-language": "zh-CN",
        "Timestamp": timestamp
    }
    # sign = createSign(data, "GET", host_url, '/linear_swap_notification', secret_key)
    sign = createSign(data, "GET", host_url, path, secret_key)
    data["op"] = "auth"
    data["type"] = "api"
    data["cid"] = '11433583'
    data["Signature"] = sign
    try:
        ws = websocket.create_connection(url + path)
        msg_str = json.dumps(data)
        print("msg_str is:", msg_str)
        ws.send(msg_str)
        msg_result = json.loads(gzip.decompress(ws.recv()).decode())
        print("msg_result is:", msg_result)
        sub_str = json.dumps(subs)
        print("sub_str is:", sub_str)
        ws.send(sub_str)
        sub_result = json.loads(gzip.decompress(ws.recv()).decode())
        print("sub_result is :", sub_result)
        ws.close()
        return sub_result
    except Exception as e:
        print("Sub failed, detail is:%s" % e)
        return {"status": "fail", "msg": "%s" % e}
def createSign(pParams, method, host_url, request_path, secret_key):
    sorted_params = sorted(pParams.items(), key=lambda d: d[0], reverse=False)
    encode_params = urllib.parse.urlencode(sorted_params)
    payload = [method, host_url, request_path, encode_params]
    payload = '\n'.join(payload)
    payload = payload.encode(encoding='UTF8')
    secret_key = secret_key.encode(encoding='UTF8')
    digest = hmac.new(secret_key, payload, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest)
    signature = signature.decode()
    return signature
def apiKeyPost(url, request_path, params, ACCESS_KEY, SECRET_KEY):
    method = 'POST'
    timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
    params_to_sign = {'AccessKeyId': ACCESS_KEY,'SignatureMethod': 'HmacSHA256','SignatureVersion': '2','Timestamp': timestamp}
    host_name = urllib.parse.urlparse(url).hostname
    host_name = host_name.lower()
    params_to_sign['Signature'] = createSign(params_to_sign, method, host_name, request_path, SECRET_KEY)
    url = url + request_path + '?' + urllib.parse.urlencode(params_to_sign)
    return request_http('post',url, params)
def timeToStamp(time_str):
    timeArray = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
def timePlus(number,times=None,types=None,period=None):
    if not times: times=datetime.datetime.now()#不传时间,则用当前时间
    else:times=datetime.datetime.strptime(times,"%Y-%m-%d %H:%M:%S")
    #功能2：获取当日凌晨开始
    if types==1: times=str(datetime.datetime.now())[:10]+' 00:00:00';times=datetime.datetime.strptime(times,"%Y-%m-%d %H:%M:%S")
    #获取时间 间隔
    if not period:                  next_time=(times+datetime.timedelta(days=number))
    elif period=='hour':        next_time=(times+datetime.timedelta(hours=number))
    elif period == 'minute': next_time = (times + datetime.timedelta(minutes=number))
    elif period == 'week':     next_time = (times + datetime.timedelta(weeks=number))
    #时间转换 标准格式
    next_time1=next_time.strftime("%Y-%m-%d %H:%M:%S")
    return next_time1
def StampToTime(timeStamp,type=None):
    if not type:
        dateArray = datetime.datetime.fromtimestamp(int(str(timeStamp)[0:]))  # 获取创建时间戳,并转换
        time = dateArray.strftime("%Y-%m-%d %H:%M:%S")  # 时间再次转换
        return  time
    if type=='MicroSecond':
        dateArray = datetime.datetime.fromtimestamp(int(str(timeStamp)[0:-3]))  # 获取创建时间戳,并转换
        time = dateArray.strftime("%Y-%m-%d %H:%M:%S")  # 时间再次转换
        return  time
def f(value,number):
    return format(value,'.'+str(number)+'f')
#截取小数点,函数名称和mysql一致
def truncate(value,number):
    a=str(value).split('.');
    if number==0: return a[0]
    if len(a)==1: return value
    else:
        if len(a[1])<number: number=len(a[1])
        l=a[1][0:number]
        return a[0]+'.'+l
