from django.conf.urls import include, url
import django.contrib.auth.views


from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'', include('bookchook.urls'))
]
