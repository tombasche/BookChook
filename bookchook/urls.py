from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from bookchook import views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'series', views.SeriesViewSet)

urlpatterns = [
    path('', include(router.urls))
]