from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("manufact/", views.maunfact_list.as_view()),
    path("manufact/<uuid:id>/", views.maunfact_detail.as_view()),
    path("currency/", views.currency_list.as_view()),
    path("currency/<int:id>/", views.currency_detail.as_view()),
    path("product/", views.product_list.as_view()),
    path("product/<uuid:id>/", views.product_detail.as_view()),
]
