from django import forms
from .models import petsitters_post, petsitters_comment

class petsittersPostForm(forms.ModelForm):
    class Meta:
        model = petsitters_post
        fields = ['title', 'content']

class petsittersCommentForm(forms.ModelForm):
    class Meta:
        model = petsitters_comment
        fields = ['content']

