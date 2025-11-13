from kafka import KafkaConsumer
import os
import json

TOPIC = os.getenv("KAFKA_TOPIC", "flask-demo-topic")
BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:19092")

def consume_forever():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="flask-sample-group",
        value_deserializer=lambda m: json.loads(m.decode("utf-8"))
    )
    print("Kafka consumer started, listening on topic:", TOPIC)
    try:
        for msg in consumer:
            print("Consumed:", msg.value)
    except KeyboardInterrupt:
        print("Stopping consumer")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_forever()
