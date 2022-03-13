from django import forms
from .models import Album

class AddForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'short_description', 'image')