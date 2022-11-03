from django.db import models
from django_countries.fields import CountryField
from django.dispatch import receiver 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from products.models import Product
# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone = models.CharField(max_length=20, null=True, blank=True)
    default_email = models.EmailField(max_length=80, null=True, blank=True)
    default_address_line_1 = models.CharField(max_length=80, null=True, blank=True)
    default_address_line_2 = models.CharField(max_length=80, null=True, blank=True)
    default_town = models.CharField(max_length=40, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=40, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def get_user_profile_details(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


#class user_wishlist(models.Model):
    
    #products = models.ManyToManyField(Product, blank=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)

    #def __str__(self):

     #   return self.user.username


