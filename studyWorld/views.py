from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def resourcesList(request):
    return render(request, 'resources/resources.html')

def resourcesIDE(request):
    return render(request, 'resources/ide.html')

def resourcesMedia(request):
    return render(request, 'resources/media.html')