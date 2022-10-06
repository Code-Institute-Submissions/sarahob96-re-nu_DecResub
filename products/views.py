from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):

    items = Product.objects.all()

    context = {
        'products': items,
    }

    return render(request, 'products/products.html', context)
