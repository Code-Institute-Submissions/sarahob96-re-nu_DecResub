from django.db import models

# Create your models here.

class Purchase(models.Models):

    order_number = models.CharField(max_length=20, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    phone = models.IntegerField(max_length=30, null=False, blank=False)
    address_line_1 = models.CharField(max_length=100, null=False, blank=False)
    address_line_2 = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=40, null=False, blank=False)
    delivery = models.DecimalField(max_digits=8, null=False, default=0)
    order_total = models.DecimalField(max_digits=12, null=False, default=0)
    grand_total = models.DecimalField(max_digits=12, null=False, default=0)
