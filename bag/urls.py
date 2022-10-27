from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_bag, name='shopping_bag'),
    path('add/<product_id>/', views.add_product, name='add_to_bag'),
    path('adjust/<product_id>/', views.adjust_quantity, name='adjust_quantity'),
    path('remove/<product_id>/', views.delete_bag_item, name='delete_bag_item'),
]