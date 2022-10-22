from django.shortcuts import render

# Create your views here.

def user_profile(request):

    template = 'profiles/profiles.html'
    context = {}

    return render(request, template, context)
