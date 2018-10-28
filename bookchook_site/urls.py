from django.conf.urls import include, url
import django.contrib.auth.views


from django.contrib import admin

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^accounts/login/$', django.contrib.auth.views.LoginView, name='login'),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url('^api/', include('bookchook.urls'))
]
