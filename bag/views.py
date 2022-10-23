from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages
# Create your views here.


def shopping_bag(request):

    return render(request, 'bag/bag.html')


def add_product(request, product_id):

    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['products_by_size'].keys():
                bag[product_id]['products_by_size'][size] += qty
            else:
                bag[product_id]['products_by_size'][size] = qty
        else:
            bag[product_id] = {'products_by_size': {size: qty}}
    else:      
        if product_id in list(bag.keys()):
            bag[product_id] += qty
        
        else:
            bag[product_id] = qty
          
    request.session['bag'] = bag
    return redirect(redirect_url)

