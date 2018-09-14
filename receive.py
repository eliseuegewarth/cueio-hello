#!/usr/bin/env python3
import pika


hello_queue = 'hello'

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


if __name__ == '__main__':

    # Connect to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue named hello_queue
    channel.queue_declare(queue=hello_queue)
    channel.basic_consume(callback,
                          queue=hello_queue,
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
