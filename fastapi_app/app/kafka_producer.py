import asyncio
import json
from aiokafka import AIOKafkaProducer
from .config import settings

async def get_producer():
    producer = AIOKafkaProducer(bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    return producer

async def produce_message(topic: str, message: dict):
    producer = await get_producer()
    try:
        await producer.send_and_wait(topic, json.dumps(message).encode("utf-8"))
    finally:
        await producer.stop()
