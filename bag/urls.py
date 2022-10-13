from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag, name="shopping_bag"),
    path("add/<product_id>/", views.add_product, name="add_to_bag"),
]