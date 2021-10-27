from django import forms
from django.forms import ModelForm
from .models import Comment, Art

class CommentForm(forms.ModelForm):  
    class Meta:  
        model = Comment  
        fields = ("name", "comment", ) 

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ['name', 'description']
