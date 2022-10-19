import json
from django.shortcuts import render, get_object_or_404, reverse
from .forms import CheckoutForm
from bag.contexts import bag_items
from django.conf import settings
from products.models import Product
import stripe
# Create your views here.

def order(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        bag = request.session.get('bag', {})

        checkout_details = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'town': request.POST['town'],
            'city': request.POST['city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            

        }
        checkout_form = CheckoutForm(checkout_details)

        if checkout_form.is_valid():
            checkout_form.save()

            request.session['save_details'] = 'save-detail' in request.POST
            return redirect(reverse('order_successful', args=[order.order_number]))

    #messages error
        users_bag = bag_items(request)
        total = users_bag['total']
        stripe_total_price = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
         amount=stripe_total_price,
         currency=settings.STRIPE_CURRENCY,
        )

    checkout_form = CheckoutForm()

    #messages error
    template = 'checkout/checkout.html'
    context = { 
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,     
    }
    return render(request, template, context)

def order_successful(request, order_number):

    save_details = request.session.get('save_details')
    order = get_object_or_404(Order, order_number=order_number)
    #success message

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/order_success.html'
    context = {
        'order': order,

    }
    return render(request, context)