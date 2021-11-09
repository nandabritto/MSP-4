from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import messages
from .models import Providers
from .forms import providerCreateForm


class ProvidersListView(ListView):
    # Displays all currently available Providers
    paginate_by = 6
    model = Providers
    template_name = 'provider-list.html'


def providers_create(request):
    # Ensuring only staff can view create page
    if request.user.is_staff:
        # View for creating a New Provider on the site
        if request.method == 'POST':
            form = providerCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'New Provider Created Successfully')
                form = providerCreateForm()
                return redirect('providers:providers-list')
        else:
            form = providerCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        return redirect('index')


def providers_update(request, pk):
    # Ensuring only staff can view amend page
    if request.user.is_staff:
        # View for Updating an existing Provider
        provider = Providers.objects.get(id=pk)
        form = providerCreateForm(instance=provider)
        if request.method == 'POST':
            form = providerCreateForm(request.POST, instance=provider)
            if form.is_valid():
                form.save()
                messages.success(request, 'Provider Updated Successfully')
                form = providerCreateForm()
                return redirect('providers:providers-list')
        context = {'form': form}
        return render(request, 'update.html', context)
    else:
        return redirect('index')


def providers_delete(request, pk):
    # Ensuring only staff can view delete page
    if request.user.is_staff:
        # View to delete an existing Provider
        provider = Providers.objects.get(id=pk)
        if request.method == "POST":
            provider.delete()
            return redirect('providers:providers-list')
        providers = providerCreateForm(instance=provider)
        context = {'providers': provider}
        return render(request, 'delete.html', context)
    else:
        return redirect('index')
