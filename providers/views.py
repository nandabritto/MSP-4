from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Providers
from .forms import providerCreateForm


# Displays all currently available exams
class ProvidersListView(ListView):
    paginate_by = 6
    model = Providers
    template_name = 'provider-list.html'

# View for creating a New Provider on the site

def providers_create(request):
  
    if request.method == 'POST':
        form = providerCreateForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            messages.success(request, 'New Provider Created Successfully')
            form = providerCreateForm()
    else:
        form = providerCreateForm()
    return render(request, 'create.html', {'form' : form})

