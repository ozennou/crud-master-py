import pika
import db
import os
import time

MQ_HOST = os.getenv('RABBIT_HOST')
MQ_USER = os.getenv('RABBITMQ_USER')
MQ_PASSWD = os.getenv('RABBITMQ_PASSWD')
RABBIT_QUEUE = os.getenv('RABBIT_QUEUE')

def main():
    try:
        connect = pika.BlockingConnection(pika.ConnectionParameters(MQ_HOST, credentials=pika.PlainCredentials(MQ_USER, MQ_PASSWD)))
        channel = connect.channel()

        def callback(ch, method, proprities, body):
            db.process_order(body)
            ch.basic_ack(delivery_tag=method.delivery_tag)


        channel.basic_consume(queue=RABBIT_QUEUE,
                            auto_ack=False,
                            on_message_callback=callback)
        channel.start_consuming()
    except StreamLostError as e:
        print("Stream connection lost, attempting to reconnect...")
        time.sleep(5)
        main()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connect.close()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()