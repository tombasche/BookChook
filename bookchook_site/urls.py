from django.conf.urls import include
import django.contrib.auth.views

from django.contrib import admin
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path(r'', admin.site.urls),
    path(r'accounts/login/', django.contrib.auth.views.LoginView, name='login'),
    path(r'jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('api/', include('bookchook.urls')),
    path('api/login/', obtain_jwt_token),
    path('api/refresh/', refresh_jwt_token)
]
