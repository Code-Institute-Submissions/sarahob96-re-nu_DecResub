from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm
from django.contrib import messages
#from checkout.models import Checkout

# Create your views here.

def user_profile(request):

    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated")
  
    form = ProfileForm(instance=profile)
    orders = profile.user_orders.all()

    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'profile_page': True 
    }
    return render(request, template, context)


def user_orders(request, order_number):

    order = get_object_or_404(Checkout, order_number=order_number)
    template = 'checkout/order_success.html'
    context = {
        'order': order,

    }
    return render(request, template, context)