from django import forms
from .models import Checkout


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ('name', 'email', 'phone', 'address_line_1', 'address_line_2',
                  'town', 'city', 'postcode', 'country', )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Full Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'address_line_1': 'Address line 1',
            'address_line_2': 'Address Line 2',
            'town': 'Town',
            'city': 'City',
            'postcode': 'Postcode',
            "country": 'Country',
        }
