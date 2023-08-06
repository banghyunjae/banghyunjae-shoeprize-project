from django.db import models
import uuid


class Manufact(models.Model):
    """
    제조사 모델
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # primary_key를 uuid로 설정, default는 고유한 uuid를 생성하도록 설정, editable은 admin 페이지에서 수정 불가능하도록 설정
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)


class Currency(models.Model):
    """
    가격 정보 모델
    """

    name = models.CharField(max_length=10)
    info = models.CharField(max_length=50, blank=True, null=True)


class Product(models.Model):
    """
    제품 모델
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )  # primary_key를 uuid로 설정, default는 고유한 uuid를 생성하도록 설정, editable은 admin 페이지에서 수정 불가능하도록 설정
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    product_code = models.CharField(max_length=10)
    manufact = models.ForeignKey(
        Manufact, on_delete=models.CASCADE, related_name="products_manufact"
    )  # 제조사와 제품은 1:N 관계, 역참조를 위해 related_name 설정
    release_date = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        default=1,
        related_name="products_currency"
        # 가격 정보와 제품은 1:N 관계, 역참조를 위해 related_name 설정, default는 id가 1인 KRW를 설정
    )
    admin_comment = models.TextField(max_length=100, blank=True, null=True)
