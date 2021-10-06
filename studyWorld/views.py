from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def ide(request):
    return render(request, 'resources/ide.html')
