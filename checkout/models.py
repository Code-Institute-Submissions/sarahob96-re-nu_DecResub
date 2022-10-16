import uuid
from django.db import models
from django.db.models import Sum
from django.conf import Settings
from django_countries.fields import CountryField

from products.models import Product

# Create your models here.

class Checkout(models.Models):

    order_number = models.CharField(max_length=20, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    phone = models.IntegerField(max_length=30, null=False, blank=False)
    address_line_1 = models.CharField(max_length=100, null=False, blank=False)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label="country", null=False, blank=False)
    postcode = models.CharField(max_length=40, null=False, blank=False)
    delivery = models.DecimalField(max_digits=8, null=False, default=0)
    order_total = models.DecimalField(max_digits=12, null=False, default=0)
    grand_total = models.DecimalField(max_digits=12, null=False, default=0)

    def create_order_number(self):
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order.number = self.create_order_number()
        super().save(*args, **kwargs)

    def update_total_cost(self):
        self.order_total = self.order.aggregate(Sum('order_total'))['order_total_total__sum'] or 0

    def __str__(self):
        return self.order_number


