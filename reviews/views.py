from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import ProductReview
from .forms import ClassReviewForm, ProductReviewForm
from products.models import Product
from profiles.models import Profile


def product_review(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            data = ProductReview()
            data.rating = form.cleaned_data['rating']
            data.title = form.cleaned_data['title']
            data.review = form.cleaned_data['review']
            data.product = product
            data.user_id = request.user.user_id
            data.save()

            return redirect(reverse('product_info', args=[product.id]))
        else:
            return redirect(reverse('product_info', args=[product.id]))
    
    else:
        form = ProductReviewForm()
    
    template = 'products/product_info.html'
    
    return render(request, template)

        