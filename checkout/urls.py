from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout_order, name='checkout'),
    path('order_success/<order_number>', views.order_successful,
         name="order_successful"),
    path('webhook/', webhook, name='webhook'),
    path('cache_checkout/', views.cache_checkout_data, name="cache_checkout"),
]
