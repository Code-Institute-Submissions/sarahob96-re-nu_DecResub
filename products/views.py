from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def products(request):

    items = Product.objects.all()

    context = {
        'products': items,
    }

    return render(request, 'products/products.html', context)

def product_info(request, product_id):

    item = get_object_or_404(Product, pk=product_id)

    context = {
        'product': item,
    }

    return render(request, 'products/product_info.html', context)
