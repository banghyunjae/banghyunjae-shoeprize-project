from rest_framework import serializers
from .models import Manufact, Currency, Product


class ManufactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufact
        fields = ["id", "name", "name_en"]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["name", "info"]


class ProductSerializer(serializers.ModelSerializer):
    """
    manufact = ManufactSerializer() # 이렇게 설정하면 manufact의 모든 정보를 받아옴
    currency = CurrencySerializer() # 이렇게 설정하면 currency의 모든 정보를 받아옴

    PirmaryKeyRelatedField를 사용한 이유는 uuid를 받아오려면 id를 받아와야하기 때문에 사용
    1. manufact와 currency를 id로 받아오기 위해서
    2. manufact와 currency를 수정할 때, id만 받아오면 되기 때문
    """

    manufact = serializers.PrimaryKeyRelatedField(queryset=Manufact.objects.all())
    currency = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all())

    class Meta:
        model = Product
        exclude = ["admin_comment"]  # admin_comment를 제외 일반인은 볼 수 없도록 설정
