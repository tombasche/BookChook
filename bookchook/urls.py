from django.conf.urls import url
import django.contrib.auth.views


from django.contrib import admin

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
]
