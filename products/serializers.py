from rest_framework import serializers
from .models import Manufact, Product


class ManufactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufact
        fields = ["id", "name", "name_en"]


class ProductSerializer(serializers.ModelSerializer):
    manufact = serializers.PrimaryKeyRelatedField(queryset=Manufact.objects.all())

    # manufact = ManufactSerializer(read_only=True)  # ManufactSerializer를 포함
    class Meta:
        model = Product
        exclude = ["admin_comment"]  # admin_comment를 제외
