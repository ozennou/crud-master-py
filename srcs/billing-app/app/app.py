import pika
import db
import os

MQ_HOST = os.getenv('RABBIT_HOST')
MQ_USER = os.getenv('RABBITMQ_USER')
MQ_PASSWD = os.getenv('RABBITMQ_PASSWD')
RABBIT_QUEUE = os.getenv('RABBIT_QUEUE')

def main():
    connect = pika.BlockingConnection(pika.ConnectionParameters(MQ_HOST, credentials=pika.PlainCredentials(MQ_USER, MQ_PASSWD)))
    channel = connect.channel()

    def callback(ch, method, proprities, body):
        db.process_order(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)


    channel.basic_consume(queue=RABBIT_QUEUE,
                        auto_ack=False,
                        on_message_callback=callback)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connect.close()

if __name__ == '__main__':
    main()