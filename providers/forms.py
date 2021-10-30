from django import forms
from .models import Providers


# Create your forms here.
class providerCreateForm(forms.ModelForm):

    class Meta:
        name = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 1}))
        description = forms.CharField(widget=forms.Textarea)
        url = forms.CharField(widget=forms.Textarea)
        model = Providers
        fields = ['name', 'description', 'url', 'logo']
        