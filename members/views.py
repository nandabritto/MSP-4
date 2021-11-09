from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterMemberForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def member_registration(request):
    # the below if will ensure page is not displayed to logged in user
    if request.user.is_authenticated:
        return redirect('index')
    else:
        # View for basic display of the registration page
        form = RegisterMemberForm()
        if request.method == 'POST':
            form = RegisterMemberForm(request.POST)
            if form.is_valid():
                form.save()
                member = form.cleaned_data.get('username')
                messages.success(request, 'Membership created for ' + member)
                return redirect('members:member-signin')

        context = {'form': form}
        return render(request, 'register.html', context)


def member_signin(request):
    # the below if will ensure page is not displayed to logged in user
    if request.user.is_authenticated:
        return redirect('index')
    else:
        # View for basic display of the login page
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'The entered details are incorrect')
        context = {}
        return render(request, 'signin.html', context)


@login_required(login_url='member-signin')
# the below if will ensure page is only displayed to logged in user
def member_signout(request):
    # View to enable member to signout
    logout(request)
    return redirect('index')
