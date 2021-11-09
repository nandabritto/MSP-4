from django import forms
from crispy_forms.helper import FormHelper
from .models import Providers


class providerCreateForm(forms.ModelForm):
    # Form to Create a new provider
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Provider Name'}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Provider description'}))
    url = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'url'}))
    logo = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(providerCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False

    class Meta:
        model = Providers
        fields = ['name', 'description', 'url', 'logo']
