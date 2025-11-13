from kafka import KafkaConsumer
import os
import json

TOPIC = os.getenv("KAFKA_TOPIC", "django-demo-topic")
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:19092")

def consume():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        auto_offset_reset="earliest",
        group_id="django-sample-group",
        value_deserializer=lambda m: json.loads(m.decode("utf-8"))
    )
    print("Kafka consumer started, listening on topic:", TOPIC)
    for msg in consumer:
        print("Consumed:", msg.value)
    consumer.close()

if __name__ == "__main__":
    consume()
