from django import forms
from .models import contact, renuReview


class contact_form(forms.ModelForm):
    """
    """

    class Meta:
        model = contact
        fields = ['name', 'your_message', 'email', 'phone']


class clubReviewForm(forms.ModelForm):

    class Meta:
        model = renuReview
        fields = ['name', 'your_experience', 'rating']
