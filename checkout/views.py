import json
from django.shortcuts import render
from .forms import CheckoutForm

from django.conf import settings 
# Create your views here.

def order(request):
    bag = request.session.get('bag', {})
    
    #messages error

    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = { 
        'checkout_form': checkout_form,
        'stripe_publishable_key': 'pk_test_51LtcVaK0jrFOpBVy2hvz7S8hYibPrZ7UISeyMK9jQ1RBQVLZUxetcW5B2Z6AP8U1yhtjmL3Edsvhv1TvnsPlOImz00wiIjCmqk',
        'client_secret': 'test client secret',      
    }
    return render(request, template, context)
