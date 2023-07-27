from rest_framework import serializers
from .models import Manufact, Product


class ManufactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
