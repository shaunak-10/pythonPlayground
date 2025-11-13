from fastapi import APIRouter
from ..kafka_producer import produce_message
from ..config import settings

router = APIRouter(prefix="/kafka", tags=["kafka"])

@router.post("/publish")
async def publish(payload: dict):
    await produce_message(settings.KAFKA_TOPIC, payload)
    return {"status": "published", "topic": settings.KAFKA_TOPIC}
