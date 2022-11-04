import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.views import Product

from profiles.models import Profile
# Create your models here.

class Checkout(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='user_orders')
    order_number = models.CharField(max_length=40, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    phone = models.IntegerField(null=False, blank=False)
    address_line_1 = models.CharField(max_length=100, null=False, blank=False)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label="country", null=False, blank=False)
    postcode = models.CharField(max_length=40, null=False, blank=False)
    delivery = models.DecimalField(max_digits=8, decimal_places=2, null=False, default=0)
    total = models.DecimalField(max_digits=12, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=12, decimal_places=2, null=False, default=0)

    def create_order_number(self):
        return uuid.uuid4().hex.upper()

    def update_total_cost(self):
        self.total = self.ordernumber.aggregate(Sum('order_total'))['order_total__sum']
        if self.total < settings.FREE_DELIVERY:
            self.delivery_cost = self.total * settings.STANDARD_DELIVERY * 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.total + self.delivery_cost
        self.save()
    
            
    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = self.create_order_number()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.order_number


class Order_number(models.Model):
    order = models.ForeignKey(Checkout, null=False, blank=False, on_delete=models.CASCADE, related_name='ordernumber')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(null=False, blank=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        self.order_total = self.product.price * self.qty
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'


