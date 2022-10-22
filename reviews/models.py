from django.db import models

from profiles.models import Profile
from products.models import Product

class ProductReview(models.Model):
    """
    Review model for users to leave a review
    """

    STARS = [(1, '1'), (2, '2'), (3, "3"), (4, "4"), (5, "5")]
    
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    review = models.TextField(max_length=400)
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(choices=STARS)


def __str__(self):
    return self.title


class ClassReview(models.Model):
    RATE = [
        (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),
    ]

    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    activity = models.CharField(max_length=50)
    review = models.TextField(max_length=400)
    rating = models.IntegerField(choices=RATE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title