from django.shortcuts import render

# View for basic display of the registration page
def member_registration(request):
    return render(request, 'register.html')