from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('resources/', views.resourcesList, name='resources-list'),
    path('resources/media', views.resourcesMedia, name='resources-media'),
    path('resources/ide', views.resourcesIDE, name='resources-ide'),
    path('resources/frameworks', views.resourcesFrameworks, name='resources-frameworks'),
    path('resources/badges', views.resourcesBadges, name='resources-badges'),
    path('resources/learning', views.resourcesLearning, name='resources-learning'),
    path('resources/tools', views.resourcesTools, name='resources-tools'),
    path('', include('exams.urls', namespace='exams')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)