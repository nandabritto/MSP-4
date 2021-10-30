from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'members'

# Members app specific urls

urlpatterns = [
    path('members/register', member_registration, name='member-register'),
    path('members/signin', member_signin, name='member-signin'),
    path('members/signout', member_signout, name='member-signout'),
]