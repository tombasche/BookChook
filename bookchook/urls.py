from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_search, name="book_search"),
    url(r'^book/new/$', views.book_new, name="book_new"),
    url(r'^book/edit/(?P<pk>\d+)/$', views.book_edit, name="book_edit"),
    url(r'^book/delete/(?P<pk>\d+)/$', views.book_delete, name="book_delete"),
    url(r'^series/new/$', views.series_new, name="series_new"),
    url(r'^user_search/$', views.user_search, name="user_search"),
    url(r'^users/$', views.user_list, name="user_list"),
    url(r'^user/new/$', views.user_new, name="user_new"),
    url(r'^user/view/(?P<pk>\d+)/$', views.user_view, name="user_view"),
    url(r'^logout$', views.logout_view, name="logout_view")
]
