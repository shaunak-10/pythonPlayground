from kafka import KafkaProducer
import json
import os

_bootstrap = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:19092")
producer = KafkaProducer(bootstrap_servers=_bootstrap,
                         value_serializer=lambda v: json.dumps(v).encode("utf-8"))

def publish_message(topic: str, message: dict):
    # synchronous send and flush
    future = producer.send(topic, message)
    producer.flush()
    # optional: check metadata
    metadata = future.get(timeout=10)
    return metadata
