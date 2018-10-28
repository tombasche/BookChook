
from rest_framework import viewsets

from bookchook.models import Book, Series
from bookchook.serializers import BookSerializer, SeriesSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed, edited or added.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class SeriesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows series to be viewed, edited or added.
    """
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
