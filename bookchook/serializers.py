from bookchook.models import Book, Series
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'author', 'user', 'status', 'series',
                  'number', 'tags', 'location', 'comment')


class SeriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Series
        fields = ('name', 'user')
