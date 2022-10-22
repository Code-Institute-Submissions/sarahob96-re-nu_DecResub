from django.shortcuts import render, get_object_or_404
from .models import Profile

# Create your views here.

def user_profile(request):

    my_profile = get_object_or_404(Profile, user=request.user)
    template = 'profiles/profiles.html'
    context = {
        'my_profile': my_profile,
    }

    return render(request, template, context)
