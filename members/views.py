from django.shortcuts import render

# View for basic display of the registration page
def member_registration(request):
    return render(request, 'register.html')

# Placeholder View for basic display of the login page
def member_signin(request):
    return render(request, 'signin.html')