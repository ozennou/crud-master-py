import pika
import json

MQ_HOST = '127.0.0.1'
MQ_USER = 'amine'
MQ_PASSWD = 'passwd'
RABBIT_EXCHANGE = 'Eorders'
RABBIT_QUEUE = 'Qorders'

def mq_sneder(data):
    params = pika.ConnectionParameters(MQ_HOST, credentials=pika.PlainCredentials(MQ_USER, MQ_PASSWD))
    connect = pika.BlockingConnection(params)
    channel = connect.channel()
    channel.basic_publish(exchange=RABBIT_EXCHANGE, routing_key='order', body=json.dumps(data))
    connect.close()
