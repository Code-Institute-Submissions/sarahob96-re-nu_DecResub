from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='checkout'),
    path('order_success/<order_number>', views.order_successful, name="order_successful"),

]