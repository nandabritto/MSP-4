from django.shortcuts import render

# View for displaying the landing page
def index(request):
    return render(request, 'index.html')

# View for displaying the resource list page
def resourcesList(request):
    return render(request, 'resources/resources.html')

# View for displaying the IDE page of the resource section
def resourcesIDE(request):
    return render(request, 'resources/ide.html')

# View for displaying the media page of the resource section
def resourcesMedia(request):
    return render(request, 'resources/media.html')

# View for displaying the framework page of the resource section
def resourcesFrameworks(request):
    return render(request, 'resources/frameworks.html')

