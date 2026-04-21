from kafka import KafkaConsumer
import json
import pandas as pd
from db_loader import insert_data

consumer = KafkaConsumer(
    "solar_topic",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

for msg in consumer:
    record = msg.value
    df = pd.DataFrame([record])
    df["status"] = df["power_kw"].apply(lambda x: "Low" if x < 10 else "High")
    insert_data(df)
