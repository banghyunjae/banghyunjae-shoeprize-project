from django.db import models
import uuid


class Manufact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    product_code = models.CharField(max_length=10)
    manufact = models.ForeignKey(Manufact, on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.DecimalField((""), max_digits=5, decimal_places=2)
    admin_comment = models.TextField(max_length=100)
