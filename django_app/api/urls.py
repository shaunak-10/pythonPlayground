from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProductViewSet, kafka_publish, external_jsonplaceholder

router = DefaultRouter()
router.register("users", UserViewSet, basename="user")
router.register("products", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
    path("kafka/publish/", kafka_publish, name="kafka-publish"),
    path("external/jsonplaceholder/", external_jsonplaceholder, name="external-jsonplaceholder"),
]
