from django.shortcuts import render, redirect, reverse
from .forms import contact_form, clubReviewForm
from .models import renuReview, contact
from django.contrib.auth import get_user
from django.contrib import messages

# Create your views here.


def form_contact(request):
    """user contact form """

    if request.method == 'POST':
        contact_fields = {

            name: request.POST('name'),
            your_message: request.POST('your_message'),
            email: request.POST('email'),
            date: request.POST('date'),
            phone: request.POST.get('phone')
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
    """Contact success page """
    return render(request, 'information/contact-success.html')


def renu_go(request):

    return render(request, 'information/renu-go.html')


def renu_form_review(request):
    """
    form view that saves review left by user
    """
    if request.method == 'POST':
        form = clubReviewForm(request.POST)
        if form.is_valid():
            data = renuReview()
            data.rating = form.cleaned_data['rating']
            data.your_experience = form.cleaned_data['your_experience']
            data.name = request.user
            data.save()
            messages.success(
                request, 'Thanks, your renu-go review has been submitted.')
            return redirect(reverse('renu-form'))
        else:
            messages.error(
                request, "Sorry, your review could not be submitted.")
            return redirect(reverse('renu-form'))
    else:
        form = clubReviewForm()

    template = 'information/renu-go.html'

    return render(request, template)


def product_admin(request):

    return render(request, 'home/product_admin.html')


def about_page(request):
    """ renders about page """
    return render(request, 'information/about.html')


def help_page(request):
    """ renders help page """
    return render(request, 'information/help.html')
