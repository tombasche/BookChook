from django import forms
from django.contrib.auth.models import User
from .models import Book, Series
from taggit.forms import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'number', 'series', 'location', 'comment')
        widgets = {
            'number' : forms.NumberInput(attrs={"class": "series-number"})
        }

class BookTagsForm(forms.Form):
    tags = forms.CharField()


class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ('name',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
