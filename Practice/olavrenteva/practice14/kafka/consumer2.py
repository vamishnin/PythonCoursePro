from kafka import KafkaConsumer
import pickle
from clientReqs import ClientReqs

consumer = KafkaConsumer(
    "complaint",
    enable_auto_commit=False,
    bootstrap_servers=["127.0.0.1:9092"],
    group_id='client_complaints_consumer',
    client_id='consumer2'
)

for message in consumer:
    with open('consumer2.log', 'a') as log:
        log.write(f'Processing client request: {pickle.loads(message.value)}\n')
        consumer.commit()
