from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_search, name="book_search"),
    url(r'^book/new/$', views.book_new, name="book_new"),
    url(r'^book/edit/(?P<pk>\d+)/$', views.book_edit, name="book_edit"),
    url(r'^book/delete/(?P<pk>\d+)/$', views.book_delete, name="book_delete"),
    url(r'^series/new/$', views.series_new, name="series_new"),
    url(r'^user/new/$', views.user_new, name="user_new"),
    url(r'^logout$', views.logout_view, name="logout_view")
]
