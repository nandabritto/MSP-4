from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponseRedirect
from .models import Providers
from .forms import providerCreateForm


# Displays all currently available exams
class ProvidersListView(ListView):
    paginate_by = 6
    model = Providers
    template_name = 'provider-list.html'

# View for displaying the framework page of the resource section
# def providersCreate(request):
#     return render(request, 'create.html')

def providers_success(request):
    return HttpResponse('successfully uploaded')

def providers_create(request):
  
    if request.method == 'POST':
        form = providerCreateForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = providerCreateForm()
    return render(request, 'create.html', {'form' : form})

# def providers_create(request):
#     if request.method == "POST":
#         form = providerCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'New Provider created successfully.')
#             return render(request, 'create.html', {'form': providerCreateForm(request.GET)})
#         else:
#             messages.error(request, 'Invalid form submission.')
#             messages.error(request, form.errors)
#     else:
#         form = providerCreateForm()
#     return render(request, 'create.html', {'form': form})




  


