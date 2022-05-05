import pika
from config.rabbitMqConfig import mqHosts

class rabbitMQ():
    def __init__(self,server,product=None):
        mqHost=mqHosts[server][product]
        self.serverIP=mqHost[0];self.serverPort=mqHost[1];self.serverUserName=mqHost[2];self.serverPassword=mqHost[3]
    #MQ发送消息
    def RabbitMQ(self,mq_exchange,mq_value,routing_key=''):
        username = 'guest'  # 指定远程rabbitmq的用户名密码  SM:productTradeStatus {"XRP":{"XRP":1}}
        pwd = 'guest'  #adim/ixkQy0d2EctBYfSB
        #queue = 'hello'
        no_ack='true'
        user_pwd = pika.PlainCredentials(self.serverUserName, self.serverPassword)
        # connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.18.6.207',port=30635,credentials=user_pwd)) #test20撮合172.18.6.207: 30616
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.serverIP,port=self.serverPort,credentials=user_pwd)) #test20撮合

        chan = connection.channel()
        # chan.queue_declare(queue='aa')  # 声明一个队列，生产者和消费者都要声明一个相同的队列，用来防止万一某一方挂了，另一方能正常运行
        chan.basic_publish(exchange=mq_exchange,  # 交换机
        routing_key = routing_key,  # 路由键，写明将消息发往哪个队列，本例是将消息发往队列hello
        body = mq_value)  # 生产者要发送的消息
        print("[send] ",mq_exchange,mq_value)
    
        # print(datetime.datetime.now(),'[消费者] waiting for msg .')
        # chan.start_consuming()  # 开始循环取消息
        connection.close()  # 当生产者发送完消息后，可选择关闭连接
