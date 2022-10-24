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

class renuReview(models.Model):
    """
    Review model for users to leave a review
    """

    STARS = ((1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"))
  
    name = models.CharField(max_length=20)
    your_experience = models.TextField(max_length=400)
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=STARS)


def __str__(self):
    return self.name
