from django.shortcuts import render


def index(request):
    # View for displaying the landing page
    return render(request, 'index.html')


def resourcesList(request):
    # View for displaying the resource list page
    return render(request, 'resources/resources.html')


def resourcesIDE(request):
    # View for displaying the IDE page of the resource section
    return render(request, 'resources/ide.html')


def resourcesMedia(request):
    # View for displaying the media page of the resource section
    return render(request, 'resources/media.html')


def resourcesFrameworks(request):
    # View for displaying the framework page of the resource section
    return render(request, 'resources/frameworks.html')


def resourcesBadges(request):
    # View for displaying the badges page of the resource section
    return render(request, 'resources/badges.html')


def resourcesLearning(request):
    # View for displaying the learning page of the resource section
    return render(request, 'resources/learning.html')


def resourcesTools(request):
    # View for displaying the tools page of the resource section
    return render(request, 'resources/tools.html')
