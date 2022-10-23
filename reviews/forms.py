from django import forms
from .models import ProductReview, ClassReview


class ProductReviewForm(forms.ModelForm):
    """
    review form for Product
    """
    class Meta:
        model = ProductReview
        fields = ['title', 'review', 'rating']

 
class ClassReviewForm(forms.ModelForm):
    """
    review form for Class
    """
   
    class Meta:
        model = ClassReview()
        fields = ['user', 'activity', 'review', 'rating']