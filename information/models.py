from django.db import models

# Create your models here.

class contact(models.Model):
    """
    contact model form
    """
    name = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    your_message = models.TextField(max_length=400)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()


def __str__(self):
    return self.name