#!/usr/bin/env python3
import pika
import time

hello_queue = 'hello'

if __name__ == '__main__':

    # Connect to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue named hello_queue
    channel.queue_declare(queue=hello_queue)

    print(' [*] Sending new messages... To exit press CTRL+C')

    i = 0
    while True:
        # Publish a message in queue hello_queue
        message = 'Message number {}'.format(i)
        channel.basic_publish(exchange='',
                              routing_key=hello_queue,
                              body=message)
        # Ok the message was sent!
        print(" [x] Sent  {}".format(message))
        i = 1 + i
        time.sleep(0.1)


    # Close the connection if you dont want to use anymore
    connection.close()
