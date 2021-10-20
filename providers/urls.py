from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from .views import (
    
# )

app_name = 'providers'

# Exam app specific urls

urlpatterns = [
    path('providers', ExamListView.as_view(), name='list-view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
