from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Providers
from .forms import providerCreateForm


# Displays all currently available Providers
class ProvidersListView(ListView):
    paginate_by = 6
    model = Providers
    template_name = 'provider-list.html'

# View for creating a New Provider on the site

def providers_create(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = providerCreateForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                messages.success(request, 'New Provider Created Successfully')
                form = providerCreateForm()
                return redirect('providers:providers-list')
        else:
            form = providerCreateForm()

        return render(request, 'create.html', {'form' : form})
    else:
        return redirect('index')

# View for Updating an existing Provider
def providers_update(request, pk):
    if request.user.is_staff:
        provider = Providers.objects.get(id=pk)
        form = providerCreateForm(instance=provider)

        if request.method == 'POST':
            form = providerCreateForm(request.POST, instance=provider)
    
            if form.is_valid():
                form.save()
                messages.success(request, 'Provider Updated Successfully')
                form = providerCreateForm()
                return redirect('providers:providers-list')

        context = {'form':form}
        return render(request, 'update.html', context)
    else:
        return redirect('index')

# Vie to delete an existing Provider
def providers_delete(request, pk):
    if request.user.is_staff:
        provider = Providers.objects.get(id=pk)
        if request.method == "POST":
            provider.delete()
            return redirect('providers:providers-list')
        providers = providerCreateForm(instance=provider)
        context = {'providers':provider}
        return render(request, 'delete.html', context)
    else:
        return redirect('index')