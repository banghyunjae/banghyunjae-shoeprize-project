from rest_framework import serializers
from .models import Manufact, Product


class ManufactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufact
        fields = ["id", "name", "name_en"]


class ProductSerializer(serializers.ModelSerializer):
    manufact = ManufactSerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "name_en", "product_code", "manufact", "release_date", "price"]
