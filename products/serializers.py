from rest_framework import serializers
from .models import Manufact, Product


class ManufactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufact
        fields = ["id", "name", "name_en"]


class ProductSerializer(serializers.ModelSerializer):
    manufact = serializers.PrimaryKeyRelatedField(
        queryset=Manufact.objects.all()
    )  # postman에서 manufact를 id로 받아옴

    # manufact = ManufactSerializer(read_only=True)
    class Meta:
        model = Product
        exclude = ["admin_comment"]  # admin_comment를 제외
