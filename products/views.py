from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q

# Create your views here.


def all_products(request):

    products = Product.objects.all()
    search_query = None

    if request.GET:
        if 's' in request.GET:
            search_query = request.GET['s']
            if not search_query:
                message.error(request, 'please enter a search item')
                return redirect(reverse('products'))
            
            search_queries = Q(name__icontains=search_query) | Q(product_description__icontains=search_query)
            products = products.filter(search_queries)
            
    context = {
        'products': products,
        'search_queries': search_query
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)
