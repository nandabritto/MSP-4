from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('exams.urls', namespace='exams')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
