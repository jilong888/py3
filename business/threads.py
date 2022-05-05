import requests,pika,random
import threading
import logging,datetime
import sys#,py_core as core
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# from common.LinearInterService import t as lit
import json
import time
def get_logger():
    logger = logging.getLogger("threading_example")
    logger.setLevel(logging.INFO)
    # fh = logging.FileHandler("threading.log")  #日志文件输出
    fh = logging.StreamHandler(sys.stdout)  #日志控制台输出 #增加sys.stdout修复日志为红的bug
    # fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    # fmt = '%(asctime)s - %(message)s'
    # fmt = ' %(message)s'
    # formatter = logging.Formatter(fmt)
    # fh.setFormatter(formatter)
    # logger.addHandler(fh)
    return logger
class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self,logger,name):
        threading.Thread.__init__(self)
        self.name = name
        self.logger = logger
    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        for i in range(3):
            ctime = time.time()
            asb = str(ctime).replace('.', '')[:16]#+str(i) +datetime.datetime.now().strftime("%S")
            print(asb)
# if __name__ == '__main__':
def start():
    #设置需要的线程数
    n = 3
    logger = get_logger()
    thread_names = locals()
    # 创建新线程
    for i in range(1, n + 1):
        thread_names['thread' + str(i)] = myThread(logger ,"线程%s" % i)
    # 开启线程
    for i in range(1, n + 1):
        thread_names['thread' + str(i)].start()
        logger.info(i)
start()