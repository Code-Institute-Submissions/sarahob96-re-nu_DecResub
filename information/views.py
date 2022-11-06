from django.shortcuts import render, redirect
from .forms import contact_form, clubReviewForm
from .models import renuReview, contact
from django.contrib.auth import get_user

# Create your views here.

def form_contact(request):
    """user contact form """

    form = contact_form()
    if request.method == 'POST':
        contact_fields = {

            'name': request.POST['name'],
            'your_message': request.POST['your_message'],
            'email': request.POST['email'],
            'date': request.POST['email'],
            'phone': request.POST['phone'],
        }
        form = contact_form(contact_fields)

        if form.is_valid():
            form.save()
            return redirect("information/contact-success.html")

    else:
        if request.user.is_authenticated:
            name = get_user(request)
            form = contact_form(initial={'name': name})

    return render(request, "information/contact.html", {'form': form})


def contact_success(request):

    return render(request, 'information/contact-success.html')
      
def renu_go(request):

    return render(request, 'information/renu-go.html')

def renu_form_review(request):
    """
    form view that saves review left by user
    """

    form = clubReviewForm()

    if request.method == 'POST':
        renu_fields = {

            'name': request.POST['name'],
            'rating': request.POST['rating'],
            'your_experience': request.POST['your_experience']
        }
        form = clubReviewForm(renu_fields)

        if form.is_valid():
            form.save()
            return redirect("information/contact-success.html")

    else:
        if request.user.is_authenticated:
            name = get_user(request)
            form = clubReviewForm(initial={'name': name})

    renu_reviews = Review.objects.all()
    return render(request, "information/renu-go.html", {'renu_reviews': renu_reviews,
                                                    'form': form})

def product_admin(request):
    
    return render(request, 'home/product_admin.html')

def about_page(request):

    return render(request, 'information/about.html')


def help_page(request):

    return render(request, 'information/help.html')