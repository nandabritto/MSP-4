from django import forms
from .models import Providers


# Form to Create a new provider
class providerCreateForm(forms.ModelForm):

    class Meta:
        model = Providers
        fields = ['name', 'description', 'url', 'logo']
        