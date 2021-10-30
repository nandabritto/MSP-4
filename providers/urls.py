from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'providers'

# Exam app specific urls

urlpatterns = [
    path('providers/', ProvidersListView.as_view(), name='providers-list'),
    path('providers/create/', providers_create, name='providers-create'),
    path('providers/update/<name>', providers_update, name='providers-update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
