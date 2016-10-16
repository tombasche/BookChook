from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.db.models import Q
from django.core.exceptions import ValidationError
from .models import Book, Series
from .forms import BookForm, SeriesForm
from taggit.forms import *

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

@login_required
def book_list(request):
    books = Book.objects.filter(user=request.user)
    return render(request, 'bookchook/book_list.html', {'books': books})

@login_required
def book_search(request):
    if request.method == "GET":
        search_query = request.GET.get('search_box', None)
        if search_query is not None:
            books = Book.objects.filter(name__icontains=search_query, user=request.user) | Book.objects.filter(tags__name__icontains=search_query, user=request.user) | Book.objects.filter(author__icontains=search_query, user=request.user) | Book.objects.filter(series__name__icontains=search_query, user=request.user).order_by('author','series__name', 'number')
            books = books.distinct() #get unique records
            return render(request, 'bookchook/book_list.html', {'books': books})
        else:
            return render(request, 'bookchook/book_search.html', {})
    books = Book.objects.filter(user=request.user).order_by('author','series__name', 'number')
    return render(request, 'bookchook/book_list.html',  {'books': books})

@login_required
def series_new(request):
    if request.method == "POST":
        form = SeriesForm(request.POST)
        if form.is_valid():
            series = form.save(commit=False)
            existingSeries = Series.objects.filter(name__icontains=series.name, user=request.user)
            if not existingSeries:
                series.user = request.user
                series.save()
                form = BookForm()
                return redirect('/book/new')
            else:
                form = SeriesForm()
                messages.error(request, "This series already exists!")
                return render(request, 'bookchook/series_form.html', {'form': form})
    else:
        form = SeriesForm()
        messages.error(request,None)
    return render(request, 'bookchook/series_form.html', {'form': form})

@login_required
def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            existingBook = Book.objects.filter(name=book.name, user=request.user)
            if not existingBook:
                book.user = request.user
                book_tags = request.POST.get('tag_box', None)
                print book.number, book.series

                if (book.number is not None and book.series is None) and book.number >= 1:
                    messages.error(request, "Book must have series in order to have a series number")
                    return render(request, 'bookchook/book_form.html', {'form': form})

                book.save()
                words = book_tags.split(",")
                for tag in words:
                    book.tags.add(tag)
                    print tag
                messages.error(request, None)
                books = Book.objects.filter(user=request.user).order_by('author','series__name', 'number')
                return render(request, 'bookchook/book_list.html',  {'books': books})
            else:
                #form = BookForm()
                messages.error(request, "This book already exists!")
                return render(request, 'bookchook/book_form.html', {'form': form})
    else:
        form = BookForm()
        messages.error(request,None)
    return render(request, 'bookchook/book_form.html', {'form': form})
