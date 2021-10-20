from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    providers_create
)

app_name = 'providers'

# Exam app specific urls

urlpatterns = [
    path('providers/create/', providers_create, name='providers-create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
