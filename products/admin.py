from django.contrib import admin
from .models import Category, Product
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


admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)