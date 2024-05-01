import pika
import time
def main():
    connect = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1', credentials=pika.PlainCredentials('amine', 'passwd')))
    channel = connect.channel()

    def callback(ch, method, proprities, body):
        print(f"message body: {body}")
        #do the work
        time.sleep(1)
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