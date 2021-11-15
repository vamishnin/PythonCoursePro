import pika
import pickle
from clientReqs import ClientReqs


connection = pika.BlockingConnection(pika.ConnectionParameters(host='0.0.0.0', port=5672))
channel = connection.channel()
channel.exchange_declare(exchange='client_requests', exchange_type='topic')
queue_name = 'complaints'
result = channel.queue_declare(queue=queue_name, exclusive=True)
channel.queue_bind(exchange='client_requests', routing_key='complaint', queue=queue_name)


def callback(ch, method, properties, body):
    with open('consumer2.log', 'a') as log:
        log.write(f'Processing client request: {pickle.loads(body)}\n')
        channel.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=False)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


