from flask_restx import Namespace, Resource, fields
from flask import request
from kafka import KafkaProducer
import json
from .config import KAFKA_BOOTSTRAP, KAFKA_TOPIC

ns = Namespace("kafka", description="Kafka operations")

payload_model = ns.model("KafkaPayload", {"message": fields.Raw(required=True)})

# one-time producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

@ns.route("/publish")
class Publish(Resource):
    @ns.expect(payload_model, validate=True)
    def post(self):
        payload = request.json.get("message", request.json)
        future = producer.send(KAFKA_TOPIC, payload)
        producer.flush()
        # get metadata (blocking)
        meta = None
        try:
            meta = future.get(timeout=10)
        except Exception as e:
            ns.abort(500, str(e))
        return {"status": "published", "topic": KAFKA_TOPIC}
