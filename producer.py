import os
import time
from kafka import KafkaProducer

bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'kafka:9092')

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

for i in range(5):
    message = f"Test message {i}".encode('utf-8')
    producer.send('test-topic', message)
    print(f"Sent: {message}")
    time.sleep(1)

producer.flush()
print("All messages sent successfully!")
