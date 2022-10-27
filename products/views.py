from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from .models import Product, Category, Product_review
from django.db.models import Q
from django.db.models.functions import Lower
from .forms import productForm, AdminProductForm
from django.contrib import messages
from django.urls import reverse_lazy
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
    product_reviews = Product_review.objects.filter(
        product_id=product.id)
    liked = False
    review_count = product_reviews.count()
     
    context = {
        'product': product,
        'product_reviews': product_reviews,
        'review_count': review_count,
        'liked': liked
    }

    return render(request, 'products/product_info.html', context)

def product_review(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            data = Product_review()
            data.title = form.cleaned_data['title']
            data.rating = form.cleaned_data['rating']
            data.review = form.cleaned_data['review']
            data.product_id = product_id
            data.user = request.user
            data.save()
            messages.success(
                request, 'Thanks, your review has been submitted.')
            return redirect(reverse('product_info', args=[product.id]))
        else:
            messages.error(
                request, "Sorry, your review could not be submitted.")
            return redirect(reverse('product_info', args=[product.id]))
    else:
        form = productForm()

    template = 'products/product_details.html'

    return render(request, template)

def delete_review(request, review_id):
    """ deletes user review """
    review = get_object_or_404(Product_review, pk=review_id)
    product = review.product

    if request.method == "POST":
        review.delete()
        messages.success(request, 'Your review has been successfully deleted')
        return redirect(reverse_lazy('product_info', args=[product.id]))

    return render(request, 'products/delete_review.html')


def update_review(request, review_id):
    """ updates the users review """
    all_reviews = get_object_or_404(Product_review, pk=review_id)
    product = all_reviews.product

    if request.method == "POST":
        form = productForm(request.POST, instance=all_reviews)
        if form.is_valid():
            form.save()
            messages.success(request, "Your review was updated")
            return redirect(reverse('product_info', args=[product.id]))
        else: 
            messages.error(request, 'sorry, we cannot update your review')
            
    else:
        form = productForm(instance=all_reviews)
    
    template = 'products/update_review.html'
    context = {
        'form': form,
        'review': all_reviews,
        'product': product
     }
    return render(request, template, context)

def add_product(request):

    if request.method == 'POST':
        form = AdminProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f' Product has been successfully added')
            return redirect(reverse('product_info', args=[product.id]))
        
        else:
            messages.error(request, f' There was an error adding product, please try again')

    else:
        form = AdminProductForm()
        
        context = {
            'form': form,
        }
    
    return render(request, 'products/add_product.html', context)


def edit_product(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = AdminProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f' product has been successfully updated')
           
            return redirect(reverse('product_info', args=[product.id]))
        
        else:
            messages.error(request, f' There was an error editing product, please try again')

    else:
        form = AdminProductForm(instance=product)
        
        context = {
            'form': form,
            'product': product,
        }
    
    return render(request, 'products/edit_product.html', context)

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f' The product was deleted')
    return redirect(reverse('products'))


def product_favourites(request, product_id, *args):
    product = get_object_or_404(Product, pk=product_id)
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)

    return HttpResponseRedirect(reverse('product_info', args=[product_id]))
