from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.conf import settings
from django.views.decorators.http import require_http_methods, require_POST

from bag.contexts import bag_items
from products.models import Product
from .forms import CheckoutForm
from .models import Checkout, Order_number
from bag.contexts import bag_items
from profiles.models import Profile
from profiles.forms import ProfileForm

import stripe
import json

#@require_POST
#def cache_checkout(request):
#    try:
      #  pid = request.POST.get('client_secret').split('_secret')[0]
       # stripe.api_key = settings.STRIPE_SECRET_KEY
       # stripe.PaymentIntent.modify(pid, metadata={
          #  'bag': json.dumps(request.session.get('bag', {})),
           # 'save_details': request.POST.get('save_details'),
           # 'username': request.user,
     #   })
        #return HttpResponse(status=200)
   # except Exception as e:
       
      #  return HttpResponse(content=e, status=400)
# error

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
            order = checkout_form.save(commit=False)

        
    #messages error
    users_bag = bag_items(request)
    total = users_bag['total']
    stripe_total_price = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total_price,
        currency=settings.STRIPE_CURRENCY,
        )

    if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = CheckoutForm(initial={
                    'name': profile.user.get_full_name,
                    'email': profile.default_email,
                    'phone_number': profile.default_phone,
                    'street_address1': profile.default_address_line_1,
                    'street_address2': profile.default_address_line_2,
                    'town': profile.default_town,
                    'city': profile.default_city,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            except Profile.DoesNotExist:
                checkout_form = CheckoutForm()
            else:
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
    checkout_order = get_object_or_404(Checkout, order_number=order_number)
    #success message

    if request.user.is_authenticated:
        profile = ProfileForm.objects.get(user=request.user)
        checkout_order.user_profile = profile
        checkout_order.save()

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/order_success.html'
    context = {
        'checkout_order': checkout_order,

    }
    return render(request, template, context)