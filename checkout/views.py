from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.conf import settings
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib import messages
from bag.contexts import bag_contents
from products.models import Product
from .forms import CheckoutForm
from .models import Checkout, Order_number
from profiles.models import Profile
from profiles.forms import ProfileForm

import stripe
import json
global intent

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_details': request.POST.get('save_details'),
            'user': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout_order(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town': request.POST['town'],
            'city': request.POST['city'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
           
        }

        checkout_form = CheckoutForm(form_data)
        if checkout_form.is_valid():
            
            order = checkout_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            for product_id, data in bag.items():
                try:
                    product = Product.objects.get(id=product_id)
                    if isinstance(data, int):
                        order_line_item = Order_number(
                            order=order,
                            product=product,
                            qty=data,
                        )
                        order_line_item.save()
                    else:
                        for size, qty in data['products_by_size'].items():
                            order_line_item = Order_number(
                                order=order,
                                product=product,
                                qty=qty,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('checkout'))

            # Save the info to the user's profile if all is well
            request.session['save_details'] = 'save-details' in request.POST
            return redirect(reverse('order_successful', args=[order.order_number]))
        else:
            print('form invalid')
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        # Attempt to prefill the form with any info the user maintains in their profile
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                checkout_form = CheckoutForm(initial={
                    'full_name': profile.user,
                    'email': profile.user.email,
                    'phone_number': profile.default_phone,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'city': profile.default_city,
                    'town': profile.default_town,
                    'street_address1': profile.default_address_line_1,
                    'street_address2': profile.default_address_line_2,
                    'country': profile.default_country,
                })
            except Profile.DoesNotExist:
                checkout_form = CheckoutForm()
        else:
            checkout_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    template = 'checkout/checkout.html'
    context = {
        'client_secret': intent.client_secret,
        'checkout_form': checkout_form,
        'stripe_public_key': stripe_public_key,
        
    }

    return render(request, template, context)


def order_successful(request, order_number):
    """
    Handle successful checkouts
    """
    save_details = request.session.get('save_details')
    order = get_object_or_404(Checkout, order_number=order_number)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_details:
            profile_data = {
                'default_phone_number': order.phone,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town': order.town,
                'default_street_address1': order.address_line_1,
                'default_street_address2': order.address_line_2,
                'default_country': order.country,
            }
            profile_form = ProfileForm(profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/order_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)

