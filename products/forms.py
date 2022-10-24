from django import forms
from .models import Product_review

class productForm(forms.ModelForm):

    class Meta:
        model = Product_review
        fields = ('title', 'review', 'rating',)
