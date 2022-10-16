from django.shortcuts import render
from .forms import CheckoutForm

# Create your views here.

def order(request):
    bag = request.session.get('bag', {})
    
    #messages error

    checkout_form = CheckoutForm()
    template = 'checkout/checkout.html'
    context = { 
        'checkout_form': checkout_form,
}
    return render(request, template, context)
    