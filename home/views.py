from django.shortcuts import render

# Create your views here.

def index(request):
    """ View that displays the home page"""
    return render(request, 'home/index.html')

