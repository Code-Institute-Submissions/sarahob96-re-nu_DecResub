from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.order, name='checkout'),
    path('order_success/<order_number>', views.order_successful, name="order_successful"),
    path('webhook/', webhook, name='webhook'),
    path('cache_checkout/', views.cache_checkout, name="cache_checkout"),
]