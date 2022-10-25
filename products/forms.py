from django import forms
from .models import Product_review, Product
from .widgets import CustomClearableFileInput

class productForm(forms.ModelForm):

    class Meta:
        model = Product_review
        fields = ('title', 'review', 'rating',)

class AdminProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)