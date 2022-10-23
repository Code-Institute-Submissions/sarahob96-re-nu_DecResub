from django import forms
from .models import contact


class contact_form(forms.ModelForm):
    """
    """

    class Meta:
        model = contact
        fields = ['name', 'your_message', 'email', 'phone']