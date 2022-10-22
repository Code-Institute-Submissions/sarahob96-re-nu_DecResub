from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone': 'Phone',
            'default_email': 'Email',
            'default_address_line_1': 'Address Line 1',
            'default_address_line_2': 'Address Line 2',
            'default_town': 'Town',
            'default_city': 'City',
            'default_postcode': 'Postcode',
            'default_country': 'Country',
        }
