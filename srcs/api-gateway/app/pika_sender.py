import pika
import json
import os

MQ_HOST = os.getenv('RABBIT_HOST')
MQ_USER = os.getenv('RABBITMQ_USER')
MQ_PASSWD = os.getenv('RABBITMQ_PASSWD')
RABBIT_EXCHANGE = os.getenv('RABBIT_EXCHANGE')

def mq_sneder(data):
    params = pika.ConnectionParameters(MQ_HOST, credentials=pika.PlainCredentials(MQ_USER, MQ_PASSWD))
    connect = pika.BlockingConnection(params)
    channel = connect.channel()
    channel.basic_publish(exchange=RABBIT_EXCHANGE, routing_key='order', body=json.dumps(data))
    connect.close()
