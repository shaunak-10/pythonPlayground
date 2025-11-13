import asyncio
import json
from aiokafka import AIOKafkaConsumer
from app.config import settings

async def consume():
    consumer = AIOKafkaConsumer(
        settings.KAFKA_TOPIC,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        group_id="fastapi-sample-group",
        auto_offset_reset="earliest",
    )
    await consumer.start()
    print("Kafka consumer started, listening on topic:", settings.KAFKA_TOPIC)
    try:
        async for msg in consumer:
            print("Consumed message:", msg.topic, msg.partition, msg.offset, msg.value.decode())
    finally:
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(consume())
