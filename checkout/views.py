from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.conf import settings
from django.views.decorators.http import require_http_methods, require_POST


from products.models import Product
from .forms import CheckoutForm
from .models import Checkout, Order_number
from profiles.models import Profile
from profiles.forms import ProfileForm

import stripe
import json


    ##stripe_public_key = settings.STRIPE_PUBLIC_KEY
    #stripe_secret_key = settings.STRIPE_SECRET_KEY

    #if request.method == "POST":
        #bag = request.session.get('bag', {})

       # checkout_details = {
    #   'name': request.POST['name'],
        #    'email': request.POST['email'],
        #    'phone': request.POST['phone'],
           # 'address_line_1': request.POST['address_line_1'],
           # 'address_line_2': request.POST['address_line_2'],
         #   'town': request.POST['town'],
          #  'city': request.POST['city'],
           # 'postcode': request.POST['postcode'],
          #  'country': request.POST['country'],
            

       # }
       # checkout_form = CheckoutForm(checkout_details)

       # if checkout_form.is_valid():
        #    order = checkout_form.save(commit=False)

         #   pid = request.POST.get('client_secret').split('_secret')[0]
         #   order.stripe_pid = pid
          #  order.original_bag = json.dumps(bag)
         #   order.save()

         #   for product_id, data in bag.contents():
             #   try:
             #       product = Product.objects.get(id=product_id)
              #      order_details = Order_number(
                 #       order=order,
                #        product=product,
                 #       qty=data,

                  #  )
                 #   order_details.save()
                #except Products.DoesNotExist:
                #    messages.error(request, (
                 #       "One of the products in your bag wasn't found in \
                 #           our database."
                  #      "Please contact us for assistance!")
                  #  )
                 #   order.delete()
                    #return redirect(reverse('view_bag'))

           # request.session['save_info'] = 'save-info' in request.POST
            #return redirect(reverse(
              # 'checkout_success', args=[order.order_number]))
      #  else:
         #  messages.error(request, 'There was an error with your form. \
            #    Please double check your information.')
    #else:
      #  bag = request.session.get('bag', {})
       # if not bag:
        #    messages.error(
             #   request, "There's nothing in your bag at the moment")
           # return redirect(reverse('products'))

        #users_bag = bag_items(request)
        #total = users_bag['total']
        #stripe_total_price = round(total * 100)
        #stripe.api_key = stripe_secret_key
    # intent = stripe.PaymentIntent.create(
        #    amount=stripe_total_price,
         #   currency=settings.STRIPE_CURRENCY,
      #  )

    #    if request.user.is_authenticated:
     #       try:
       #         profile = Profile.objects.get(user=request.user)
         #       order_form = CheckoutForm(initial={
             #       'name': profile.user.get_full_name,
              #      'email': profile.default_email,
               #     'phone_number': profile.default_phone,
              #      'street_address1': profile.default_address_line_1,
             #       'street_address2': profile.default_address_line_2,
               #     'town': profile.default_town,
              #      'city': profile.default_city,
              #      'postcode': profile.default_postcode,
              #      'country': profile.default_country,
               #             })
         #   except Profile.DoesNotExist:
            #    checkout_form = CheckoutForm()
        #else:
          #  checkout_form = CheckoutForm()

    #messages error
       # template = 'checkout/checkout.html'
       # context = { 
           #         'checkout_form': checkout_form,
           #         'stripe_public_key': stripe_public_key,
            #        'client_secret': intent.client_secret,     
            #        }
      # return render(request, template, context)

#def order_successful(request, order_number):

 #   save_details = request.session.get('save_details')
  #  checkout_order = get_object_or_404(Checkout, order_number=order_number)
    #success message

   # if request.user.is_authenticated:
   #     profile = ProfileForm.objects.get(user=request.user)
   #     checkout_order.user_profile = profile
     #   checkout_order.save()

   # if 'bag' in request.session:
      #  del request.session['bag']
##
   # template = 'checkout/order_success.html'
   # context = {
    #    'checkout_order': checkout_order,
#
   # }
   # return render(request, template, context)


def checkout(request):
   bag = request.session.get('bag', {})
   if not bag:
      messages.error(request, "There's nothing in your bag")
      return redirect(reverse('products'))

   checkout_form = CheckoutForm()
   template = "checkout/checkout.html"
   context = {
      'checkout_form': checkout_form,
      'stripe_public_key': 'pk_test_51LtcVaK0jrFOpBVy2hvz7S8hYibPrZ7UISeyMK9jQ1RBQVLZUxetcW5B2Z6AP8U1yhtjmL3Edsvhv1TvnsPlOImz00wiIjCmqk',
      'client_secret': 'test client_secret',
   }
   return render(request, template, context)