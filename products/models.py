from django.db import models


class Manufact(models.Model):
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    product_code = models.CharField(max_length=10)
    manufact = models.ForeignKey(Manufact, on_delete=models.CASCADE)
    release_date = models.DateField()
    price = models.DecimalField((""), max_digits=5, decimal_places=2)
    admin_comment = models.TextField(max_length=100)
