from kafka import KafkaConsumer
import pickle
from clientReqs import ClientReqs

consumer = KafkaConsumer(
    "question",
    enable_auto_commit=False,
    bootstrap_servers=["127.0.0.1:9092"],
    group_id='client_questions_consumer',
    client_id='consumer1'
)

for message in consumer:
    with open('consumer1.log', 'a') as log:
        log.write(f'Processing client request: {pickle.loads(message.value)}\n')
        consumer.commit()
