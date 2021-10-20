from django import forms
from .models import Providers


# Create your forms here.
class providerForm(forms.ModelForm):

    class Meta:
        model = Providers
        fields = ('name', 'description', 'url', 'image')