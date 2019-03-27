from django.conf.urls import include
import django.contrib.auth.views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(r'', admin.site.urls),
    path(r'accounts/login/', django.contrib.auth.views.LoginView, name='login'),
    path(r'jet/', include('jet.urls', 'jet')),  # Django JET URLS
]