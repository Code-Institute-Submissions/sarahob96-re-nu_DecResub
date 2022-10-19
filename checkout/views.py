import json
from django.shortcuts import render
from .forms import CheckoutForm
from bag.contexts import bag_items
from django.conf import settings
import stripe
# Create your views here.

def order(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    
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
