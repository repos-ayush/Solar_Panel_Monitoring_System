from kafka import KafkaProducer
import json, time
from sensor_simulator import generate_data

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    data = generate_data()
    producer.send("solar_topic", data)
    print("Sent:", data)
    time.sleep(2)
