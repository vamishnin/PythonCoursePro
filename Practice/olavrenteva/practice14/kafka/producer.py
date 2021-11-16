from kafka import KafkaProducer
import pickle
from clientReqs import ClientReqs


client_reqs = [
    ClientReqs('Ivanov', 'question', 'Ivanov.Question#1'),
    ClientReqs('Petrov', 'question', 'Petrov.Question#1'),
    ClientReqs('Petrov', 'complaint', 'Petrov.Complaint#1')
]


producer = KafkaProducer(bootstrap_servers="127.0.0.1:9092")

for req in client_reqs:
    producer.send(req.request_type.lower(), pickle.dumps(req))
    print(f'{req} is send to kafka')

producer.flush()
