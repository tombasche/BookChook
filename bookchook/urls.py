from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_search, name="book_search"),
    url(r'^book/new/$', views.book_new, name='book_new'),
]
