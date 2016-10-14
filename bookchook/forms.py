from django import forms
from .models import Book, Series
from taggit.forms import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'series')

class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ('name','number')
