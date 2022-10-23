from django import forms
from .models import ProductReview, ClassReview


class ProductReviewForm(forms.ModelForm):
    """
    review form for Product
    """
    class Meta:
        model = ProductReview
        exclude = (
            'user',
            'date',
            'product',
        )

        fields = ['title', 'review', 'rating']

        labels = {
            'rating': 'Rating',
        }
    
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Description',
        }

        #self.fields['title'].widget.attrs['autofocus'] = True
        #for field in self.fields:
            
         #   if field != 'rating':
           #     placeholder = placeholders[field]
              # self.fields[field].widget.attrs['placeholder'] = placeholder
               # self.fields[field].label = False


class ClassReviewForm(forms.ModelForm):
    """
    review form for Class
    """
   
    class Meta:
        model = ClassReview()
        fields = ['user', 'activity', 'review', 'rating']