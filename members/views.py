from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterMemberForm

from django.contrib.auth import authenticate, login, logout

# View for basic display of the registration page
def member_registration(request):
    form = RegisterMemberForm()

    if request.method == 'POST':
        form = RegisterMemberForm(request.POST)
        if form.is_valid():
            form.save()
            member = form.cleaned_data.get('username')
            messages.success(request, 'Membership created for ' + member)
            return redirect('members:member-signin')

    context = {'form':form}
    return render(request, 'register.html', context)

# Placeholder View for basic display of the login page
def member_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
    context = {}
    return render(request, 'signin.html', context)