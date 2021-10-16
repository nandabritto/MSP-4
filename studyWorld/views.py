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

# View for displaying the badges page of the resource section
def resourcesBadges(request):
    return render(request, 'resources/badges.html')

# View for displaying the learning page of the resource section
def resourcesLearning(request):
    return render(request, 'resources/learning.html')

# View for displaying the tools page of the resource section
def resourcesTools(request):
    return render(request, 'resources/tools.html')