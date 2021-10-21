from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Providers
from django.contrib.auth.models import User
from .forms import providerCreateForm


# Displays all currently available exams
class ProvidersListView(ListView):
    model = Providers
    template_name = 'provider-list.html'

# View for displaying the framework page of the resource section
# def providersCreate(request):
#     return render(request, 'create.html')

def providers_create(request):
  
    if request.method == 'POST':
        form = providerCreateForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = providerCreateForm()
    return render(request, 'create.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')

