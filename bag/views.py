from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

# Create your views here.


def shopping_bag(request):

    return render(request, 'bag/bag.html')

