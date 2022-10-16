from django.shortcuts import get_object_or_404
from products.models import Product


def bag_items(request):

    bag_contents = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, qty in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total += qty * product.price
        product_count += qty
        bag_contents.append({
            'product_id': product_id,
            'qty': qty,
            'product': product, 
        })
        individual_total = qty * product.price
    context = {
        'bag_contents': bag_contents,
        'total': total,
        'product_count': product_count,
        'qty': qty,
        'individual_total': individual_total,

    }
    return context

