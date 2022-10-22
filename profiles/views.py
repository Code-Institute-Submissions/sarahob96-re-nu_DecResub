from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm

# Create your views here.

def user_profile(request):

    return render(request, 'profiles/profiles.html')

def user_orders(request):
    my_profile = get_object_or_404(Profile, user=request.user)
    #'orders': ordersform = ProfileForm(instance=my_profile)