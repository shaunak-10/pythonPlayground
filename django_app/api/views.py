from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer, KafkaPublishSerializer, JsonPlaceholderResponseSerializer
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from .kafka_producer import publish_message
import requests
from django.conf import settings
import os

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.using("default").all()

    def perform_create(self, serializer):
        # serializer.create handles using("default")
        instance = serializer.save()
        serializer.instance = instance

    def perform_update(self, serializer):
        instance = serializer.save()
        serializer.instance = instance

    def perform_destroy(self, instance):
        User.objects.using("default").filter(pk=instance.pk).delete()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.using("mysql_db").all()

    def perform_create(self, serializer):
        # serializer.create handles using("mysql_db")
        instance = serializer.save()   # safe now because create() uses .using("mysql_db")
        serializer.instance = instance

    def perform_update(self, serializer):
        # serializer.update handles saving to mysql_db
        instance = serializer.save()
        serializer.instance = instance

    def perform_destroy(self, instance):
        # delete from the mysql_db explicitly
        Product.objects.using("mysql_db").filter(pk=instance.pk).delete()


# Kafka publish endpoint as an API view
@extend_schema(
    request=KafkaPublishSerializer,
    responses={200: dict}
)
@api_view(["POST"])
def kafka_publish(request):
    payload = request.data if isinstance(request.data, dict) else {}
    topic = os.getenv("KAFKA_TOPIC", "django-demo-topic")
    try:
        publish_message(topic, payload)
        return Response({"status": "published", "topic": topic})
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# External API proxy
@extend_schema(
    responses=JsonPlaceholderResponseSerializer
)
@api_view(["GET"])
def external_jsonplaceholder(request):
    r = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
    r.raise_for_status()
    return Response(r.json())
