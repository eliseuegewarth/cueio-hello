#!/usr/bin/env python3
import pika
import time


hello_queue = 'hello'


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(len(body)*0.1)
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


if __name__ == '__main__':

    # Connect to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue named hello_queue
    channel.queue_declare(queue=hello_queue)

    # Tells that can handle 1 message per time
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(callback,
                          queue=hello_queue)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
