from django.shortcuts import render, get_object_or_404
from .models import Profile
from .forms import ProfileForm

# Create your views here.

def user_profile(request):

    my_profile = get_object_or_404(Profile, user=request.user)

    form = ProfileForm(instance=my_profile)
    #orders = my_profile.orders.all()
    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'my_profile': my_profile,
        #'orders': orders
    }

    return render(request, template, context)
