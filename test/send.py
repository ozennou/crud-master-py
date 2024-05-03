import pika
import json

data = {'user_id': 10, 'number_of_items': 15, 'total_amount': 520}

message=json.dumps(data)

connect = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', credentials=pika.PlainCredentials('amine', 'passwd')))
channel = connect.channel()
channel.basic_publish(exchange='Eorders',
                      routing_key='order',
                      body=message)


connect.close()