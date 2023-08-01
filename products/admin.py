from django.contrib import admin
from .models import Manufact, Currency, Product


"""
관리자 페이지에서도 제조사, 가격 정보, 제품을 볼 수 있도록 설정
수정, 삭제, 추가 가능
"""


class ManufactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "name_en")


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("name", "info")


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "name_en",
        "product_code",
        "manufact",
        "release_date",
        "price",
        "currency",
        "admin_comment",
    )


admin.site.register(Manufact, ManufactAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Product, ProductAdmin)
