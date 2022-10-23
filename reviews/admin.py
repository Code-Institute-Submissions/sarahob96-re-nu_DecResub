from django.contrib import admin
from .models import ProductReview
# Register your models here.

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
        'title',
        'review',

    )

admin.site.register(ProductReview, ProductReviewAdmin)