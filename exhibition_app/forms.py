from django.forms import ModelForm
from .models import Art

class ArtForm(ModelForm):
    class Meta:
        model = Art
        fields = ['name', 'description']