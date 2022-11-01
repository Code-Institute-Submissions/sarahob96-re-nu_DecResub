from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_bag(request):
    """ A view that renders the shopping bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the product to the shopping bag """
    product = Product.objects.get(pk=product_id)
    qty = int(request.POST.get('qty'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    (print(qty))
    
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if product_id in list(bag.keys()):
            if size in bag[product_id]['products_by_size'].keys():
                bag[product_id]['products_by_size'][size] += qty
                messages.success(request, f'Added {product.name} to your bag')
            else:
                bag[product_id]['products_by_size'][size] = qty
                messages.success(request, f'Added {product.name} to your bag')
        else:
            bag[product_id] = {'products_by_size': {size: qty}}
            messages.success(request, f'Added {product.name} to your bag')
    else:
        if product_id in list(bag.keys()):
            bag[product_id] += qty
            messages.success(
                request, f'Updated {product.name} quantity to {bag[product_id]}')
        else:
            bag[product_id] = qty
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)
    

def adjust_quantity(request, product_id):

    qty = int(request.POST.get('qty'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if qty > 0:
            bag[product_id]['products_by_size'][size] = qty
        else:
            del bag[product_id]['products_by_size'][size]
            if not bag[product_id]['products_by_size']:
                bag.pop(product_id)
    else:
        if qty > 0:
            bag[product_id] = qty
        else:
            bag.pop(product_id)
            messages.success(request, f'Your bag has been updated')

    request.session['bag'] = bag
    return redirect(reverse('shopping_bag'))


def delete_bag_item(request, product_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[product_id]['products_by_size'][size]
            if not bag[product_id]['products_by_size']:
                bag.pop(product_id)
        else:
            bag.pop(product_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)