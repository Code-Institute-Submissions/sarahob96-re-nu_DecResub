from django.urls import path
from . import views

urlpatterns = [
    path('/contact', views.form_contact, name="form_contact"),
    path('contact-success', views.contact_success, name="contact-success"),
    path('renu-go', views.renu_go, name="renu-go"),
    path('', views.renu_form_review, name="renu-form"),
    path('', views.product_admin, name="admin"),
    path('about/', views.about_page, name="about"),
    path('help/', views.help_page, name="help")
]