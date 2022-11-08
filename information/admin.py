from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import renuReview,  contact


@admin.register(renuReview)
class RenuReviewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'your_experience',
        'date',
        'rating',
    )


@admin.register(contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'your_message',
        'email',
        'phone',
    )