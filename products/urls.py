from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<int:product_id>/', views.product_info, name='product_info'),
    path('product_review/<int:product_id>/', views.product_review, name='product_review'),
    path('update_review/<int:review_id>/', views.update_review, name='update_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('add_product', views.add_product, name='add_product'),
]
