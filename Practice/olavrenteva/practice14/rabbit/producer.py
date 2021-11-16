import pika
import pickle
from clientReqs import ClientReqs

client_reqs = [
    ClientReqs('Ivanov', 'question', 'Ivanov.Question#1'),
    ClientReqs('Petrov', 'question', 'Petrov.Question#1'),
    ClientReqs('Petrov', 'complaint', 'Petrov.Complaint#1')
]


connection = pika.BlockingConnection(pika.ConnectionParameters(host='0.0.0.0', port=5672))
channel = connection.channel()
channel.exchange_declare(exchange='client_requests', exchange_type='topic')

for req in client_reqs:
    channel.basic_publish(exchange='client_requests',
                          routing_key=req.request_type.lower(),
                          body=pickle.dumps(req))
    print(f'{req} is send to exchange')
connection.close()
