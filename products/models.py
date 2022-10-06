from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    category_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
  
    def get_category_name(self):
        return self.category_name
   

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    product_description = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image_url = models.URLField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

