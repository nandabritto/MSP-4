from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Providers
from django.contrib.auth.models import User



def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'main/upload.html', {'file_url': file_url})
    return render(request, 'main/upload.html')