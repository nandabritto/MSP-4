from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'members'

# Exam app specific urls

urlpatterns = [
    path('members/', member_registration, name='member-register'),
]