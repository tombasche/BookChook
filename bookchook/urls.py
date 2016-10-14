from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_search, name="book_search"),
    url(r'^book/new/$', views.book_new, name="book_new"),
    url(r'^series/new/$', views.series_new, name="series_new"),
    url(r'^logout$', views.logout_view, name="logout_view")
]
