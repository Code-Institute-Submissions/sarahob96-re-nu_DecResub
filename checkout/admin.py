from django.contrib import admin
from .models import Checkout, Order_number

# Register your models here.


class CheckoutAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'delivery', 'total', 
                       'grand_total')

    fields = ('order_number', 'date', 'name', 'phone', 'address_line_1', 
              'address_line_2', 'town', 'city', 'country', 'postcode', 
              'delivery', 'total', 'grand_total')

    order_list = ('order_number', 'date', 'name', 'grand_total')  

    sorting = ('-date,')


admin.site.register(Checkout, CheckoutAdmin)