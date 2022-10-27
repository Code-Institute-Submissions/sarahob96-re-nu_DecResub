from django.shortcuts import render

# Create your views here.

def index(request):
    """ View that displays the home page"""
    return render(request, 'home/index.html')

def error_404(request, *args, **argv):
    """View to return 404 error page 
    """
    return render(request, 'home/404.html')  