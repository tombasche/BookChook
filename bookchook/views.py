
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from bookchook.models import Book, Series
from bookchook.serializers import BookSerializer, SeriesSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed, edited or added.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SeriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows series to be viewed, edited or added.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
