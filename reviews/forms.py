from django import forms
from .models import ProductReview, ClassReview


class ProductReviewForm(forms.ModelForm):
    """
    review form for Product
    """
    def __init__(self, *args, **kwargs):
        super(ProductReviewForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = ProductReview
        fields = ['user', 'product', 'title', 'review', 'date', 'rating']

    
class ClassReviewForm(forms.ModelForm):
    """
    review form for Class
    """
    def __init__(self, *args, **kwargs):
        super(ClassReviewForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['readonly'] = True

    class Meta:
        model = ClassReview()
        fields = ['user', 'activity', 'review', 'rating', 'date']