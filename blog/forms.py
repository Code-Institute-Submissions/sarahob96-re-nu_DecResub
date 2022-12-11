from django import forms
from .models import Comment


class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'comment')

    def __init__(self, *args, **kwargs):
        super(commentForm, self).__init__(*args, **kwargs)
       
