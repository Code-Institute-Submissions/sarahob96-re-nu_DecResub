from django.contrib import admin
from .models import Category, Product, Product_review
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'sku',
        'price',
        'image',
    )


class AdminCategory(admin.ModelAdmin):
    list_display = (
        'category_name',
        'name'
    )



class ReviewAdmin(admin.ModelAdmin):
    """Admin Panel display for Product Model"""
    list_display = (
        'product',
        'title',
        'user',
        'rating',
        'review',
        
    )


admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Product_review, ReviewAdmin)