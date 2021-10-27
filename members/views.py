from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterMemberForm

# View for basic display of the registration page
def member_registration(request):
    form = RegisterMemberForm()

    if request.method == 'POST':
        form = RegisterMemberForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'register.html', context)

# Placeholder View for basic display of the login page
def member_signin(request):
    return render(request, 'signin.html')