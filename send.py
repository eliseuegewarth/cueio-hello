#!/usr/bin/env python3
import pika

if __name__ == '__main__':

    # Connect to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue named 'hello'
    channel.queue_declare(queue='hello')

    # Publish a message in queue 'hello'
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')

    # Ok the message was sent!
    print(" [x] Sent 'Hello World!'")

    # Close the connection if you dont want to use anymore
    connection.close()
