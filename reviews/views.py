from django.shortcuts import render, get_object_or_404

from .models import ProductReview
from .forms import ClassReviewForm, ProductReviewForm
from products.models import Product
from profiles.models import Profile


def product_review(request, product_id):

    user = Profile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    product_review_form = ProductReviewForm()
    review_fields = {
        'title': request.POST['title'],
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }

    product_review_form = ProductReviewForm(review_fields)

    if product_review_form is valid():
        item_review = product_review_form.save(commit=False)
        item_review.user = user
        item_review.product = product
        item_review.save()

        item_reviews = ProductReview.objects.filter(product=product)
        product.save()

        messages.success(request, "Thanks for leaving a review!")
    
    else:
        messages.error(request, "Sorry, your review could not be added. Please make sure form is filled in")

    return redirect(reverse('product_info', args=(product_id,)))
