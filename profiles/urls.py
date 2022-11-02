from django.urls import path
from . import views

urlpatterns = [
  path('', views.user_profile, name="profile"),
  path('user_orders/<order_number>', views.user_orders, name="user_orders"),

]