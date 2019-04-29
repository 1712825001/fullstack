import pika

# connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.174.128', port=5672, ))
# channel = connection.channel()
# channel.queue_declare(queue='test')
# channel.basic_publish(exchange='', routing_key='test', body='Hello World!')
# print('send success msg to rabbitmq')
# connection.close()   #关闭连接
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.174.128',port=5672,))