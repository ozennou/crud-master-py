import pika
import db

def main():
    connect = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq', credentials=pika.PlainCredentials('amine', 'passwd'))) #replace the user and passwd
    channel = connect.channel()

    def callback(ch, method, proprities, body):
        db.process_order(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)


    channel.basic_consume(queue='Qorders',
                        auto_ack=False,
                        on_message_callback=callback)
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connect.close()

if __name__ == '__main__':
    main()