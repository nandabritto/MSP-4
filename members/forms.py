from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterMemberForm(UserCreationForm):
    # For enables members to register
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
