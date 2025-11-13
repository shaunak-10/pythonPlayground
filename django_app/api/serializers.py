from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email"]

    def create(self, validated_data):
        # ensure creation on Postgres (default)
        return User.objects.using("default").create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save(using="default")
        return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]

    def create(self, validated_data):
        # create directly on the mysql_db using the DB router
        return Product.objects.using("mysql_db").create(**validated_data)

    def update(self, instance, validated_data):
        # update fields on instance and save to mysql_db
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save(using="mysql_db")
        return instance

class KafkaPublishSerializer(serializers.Serializer):
    message = serializers.DictField()

class JsonPlaceholderResponseSerializer(serializers.Serializer):
    userId = serializers.IntegerField(required=False)
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(required=False)
    completed = serializers.BooleanField(required=False)

