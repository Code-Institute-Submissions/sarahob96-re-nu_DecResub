from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.db.models.functions import Lower


# Create your views here.


def all_products(request):

    products = Product.objects.all()
    search_query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sorting = request.GET['sort']
            sort = sorting
            if sorting == 'name':
                sorting= 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sorting == 'renu_category':
                sorting = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'descending':
                    sorting = f'-{sorting}'
            products = products.order_by(sorting)

    if request.GET:

        if 'renu_category' in request.GET:
            categories = request.GET['renu_category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 's' in request.GET:
            search_query = request.GET['s']
            if not search_query:
                message.error(request, 'please enter a search item')
                return redirect(reverse('products'))

            search_queries = Q(name__icontains=search_query) | Q(product_description__icontains=search_query)
            products = products.filter(search_queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_queries': search_query,
        'active_category': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_info(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_info.html', context)

