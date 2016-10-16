from django import forms
from .models import Book, Series
from taggit.forms import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'number', 'series', 'location')
        widgets = {
            'series' : forms.Select(attrs={"onChange":'displaySeriesNumber()'}),
            'number' : forms.NumberInput(attrs={"class": "series-number"})
        }


class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ('name',)
