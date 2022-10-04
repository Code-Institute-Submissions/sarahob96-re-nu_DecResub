from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    category_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_category_name(self):
        return self.category_name