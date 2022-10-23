from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal 
from django.conf import settings 

def bag_items(request):

    bag_contents = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    grand_total = 0

    for product_id, data in bag.items():
        if isinstance(data, int):
            product = get_object_or_404(Product, pk=product_id)
            total += data * product.price
            product_count += data
            bag_contents.append({
                'product_id': product_id,
                'qty': data,
                'product': product, 
            })
        else:
            product = get_object_or_404(Product, pk=product_id)
            for size, qty in data['products_by_size'].items():
                total += qty * product.price
                product_count += qty
                bag_contents.append({
                    'product_id': product_id,
                    'qty': qty,
                    'product': product,
                    'size': size,
                })
    grand_total = total+5
    context = {
        'bag_contents': bag_contents,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total
   
    }
    return context

