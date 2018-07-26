
# coding: utf-8
# @Author: sharpen
# @Date: 2018.07.26
# @Desc: ''' 体验简单的mq的发布、消费（推拉）

import pika

credentials = pika.PlainCredentials('sharpenhw', 'Monica216')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='49.4.23.115', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()