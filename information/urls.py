from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_contact, name="form_contact"),
    path('', views.contact_success, name="contact-success")
]