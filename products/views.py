from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):

    items = Product.objects.all()

    return render(request, 'products/products.html', {'items': items})