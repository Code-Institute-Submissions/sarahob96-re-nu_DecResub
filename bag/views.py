from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages
# Create your views here.


def shopping_bag(request):

    return render(request, 'bag/bag.html')


def add_product(request, product_id):

    product = Product.objects.get(pk=product_id)
    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')
    #size = None
    #if 'product_size' in request.POST:
      #  size = request.POST['product_size']
    bag = request.session.get('bag', {})

    #if size:
     #   if product_id in list(bag.keys()):
         #   if size in bag[product_id]['products_by_size'].keys():
          #      bag[product_id]['products_by_size'][size] += qty
         #   else:
         #       bag[product_id]['products_by_size'][size] = qty
        #else:
         #   bag[product_id] = {'products_by_size': {size: qty}}
            
    if product_id not in list(bag.keys()):
        bag[product_id] = qty
        messages.success(request, f'Added {product.name} to the bag')

    else:
        bag[product_id] += qty
        messages.success(request, f' {product.name} quantity has been updated')
    request.session['bag'] = bag
    return redirect(redirect_url)

