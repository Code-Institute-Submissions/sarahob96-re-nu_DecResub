from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages
# Create your views here.


def shopping_bag(request):

    return render(request, 'bag/bag.html')


def add_product(request, product_id):

    product = Product.objects.get(pk=product_id)
    qty = request.POST.get('qty')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id not in list(bag.keys()):
        bag[product_id] = int(qty)
    else:
        bag[product_id] += int(qty)
        messages.success(request, f'Added {product.name} to the bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

