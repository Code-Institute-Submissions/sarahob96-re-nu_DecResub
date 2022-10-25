from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm
from checkout.models import Checkout

# Create your views here.

def user_profile(request):

    return render(request, 'profiles/profiles.html')

def user_orders(request, order_number):

    user_orders = get_object_or_404(Checkout, order_number=order_number)
    template = 'checkout/order_success.html'
    context = {
        'user_orders': user_orders,

    }
    return render(request, template, context)