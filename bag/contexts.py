from decimal import Decimal
from django.conf import settings 
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    for product_id, data in bag.items():
        if isinstance(data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += data * product.price
            product_count += data
            bag_items.append({
                'product_id': product_id,
                'qty': data,
                'product': product,
            })

        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, qty in data['products_by_size'].items():
                total += qty * product.price
                product_count += qty
                bag_items.append({
                    'product_id': product_id,
                    'qty': qty,
                    'product': product,
                    'size': size,
                })
 

    if total < settings.FREE_DELIVERY:
        delivery_cost = total * Decimal(settings.STANDARD_DELIVERY / 100)
        free_delivery_remainder = settings.FREE_DELIVERY - total
    else:
        delivery_cost = 0
        free_delivery_remainder = 0

    grand_total = delivery_cost + total 
    bag = request.session.get('bag', {})  

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery_cost': delivery_cost,
        'free_delivery_remainder': free_delivery_remainder,
        'free_delivery': settings.FREE_DELIVERY,
        'grand_total': grand_total,
    }

    return context


