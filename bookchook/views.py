from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.db.models import Q
from django.core.exceptions import ValidationError
from .models import Book, Series
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import BookForm, SeriesForm, BookTagsForm, UserForm
from taggit.forms import *

SEARCH_RESULTS = None


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

@login_required
def book_list(request):
    global SEARCH_RESULTS
    SEARCH_RESULTS = Book.objects.filter(user=request.user)
    return render(request, 'bookchook/book_list.html', {'books': SEARCH_RESULTS})

@login_required
def book_search(request):
    if request.method == "GET":
        search_query = request.GET.get('search_box', None)
        if search_query is not None:
            global SEARCH_RESULTS
            SEARCH_RESULTS = Book.objects.filter(name__icontains=search_query, user=request.user) | Book.objects.filter(tags__name__icontains=search_query, user=request.user) | Book.objects.filter(author__icontains=search_query, user=request.user) | Book.objects.filter(series__name__icontains=search_query, user=request.user).order_by('author','series__name', 'number')
            global SEARCH_RESULTS
            SEARCH_RESULTS = SEARCH_RESULTS.distinct() #get unique records
            return render(request, 'bookchook/book_list.html', {'books': SEARCH_RESULTS})
        else:
            return render(request, 'bookchook/book_search.html', {})
    global SEARCH_RESULTS
    SEARCH_RESULTS = Book.objects.filter(user=request.user).order_by('author','series__name', 'number')
    return render(request, 'bookchook/book_list.html',  {'books': SEARCH_RESULTS})

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
    form = BookForm()
    tagForm = BookTagsForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            existingBook = Book.objects.filter(name=book.name, user=request.user)
            if not existingBook:
                book.user = request.user
                book_tags = request.POST.get('tags', None)

                if (book.number is not None and book.series is None) and book.number >= 1:
                    messages.error(request, "Book must have series in order to have a series number")
                    return render(request, 'bookchook/book_form.html', {'form': form})

                book.save()
                words = book_tags.split(",")
                for tag in words:
                    book.tags.add(tag)

                messages.error(request, None)
                global SEARCH_RESULTS
                SEARCH_RESULTS = Book.objects.filter(user=request.user).order_by('author','series__name', 'number')
                return render(request, 'bookchook/book_list.html',  {'books': SEARCH_RESULTS})
            else:
                #form = BookForm()
                messages.error(request, "This book already exists!")
                return render(request, 'bookchook/book_form.html', {'form': form})
    else:
        form = BookForm()
        tagForm = BookTagsForm()
        messages.error(request,None)
    return render(request, 'bookchook/book_form.html', {'form': form, 'tags': tagForm})

@login_required
def book_edit(request, pk):
    editBook = Book.objects.get(id=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=editBook)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = editBook.user
            book_tags = request.POST.get('tags', None)
            print book_tags
            if (book.number is not None and book.series is None) and book.number >= 1:
                messages.error(request, "Book must have series in order to have a series number")
                return render(request, 'bookchook/book_form.html', {'form': form})

            book.save()
            words = book_tags.split(",")
            for tag in words:
                book.tags.add(tag)

            messages.error(request, None)
            global SEARCH_RESULTS
            SEARCH_RESULTS = Book.objects.filter(user=request.user).order_by('author','series__name', 'number')
            return render(request, 'bookchook/book_list.html',  {'books': SEARCH_RESULTS})
    else:
        book = Book.objects.get(id=pk)
        form = BookForm(instance=book)
        finalTags = ",".join(list(book.tags.all().values_list('name', flat=True)))

        tagForm = BookTagsForm(initial={'tags': finalTags})
        book = Book.objects.get(id=pk)
        messages.error(request,None)

    return render(request, 'bookchook/book_form.html', {'form': form, 'tags':tagForm})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    Book.objects.filter(id=book.id).delete()
    global SEARCH_RESULTS
    SEARCH_RESULTS = SEARCH_RESULTS.exclude(id=book.id)
    return render(request, 'bookchook/book_list.html',  {'books': SEARCH_RESULTS})

def user_new(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return render(request, 'bookchook/book_list.html', {})
    else:
        form = UserForm()
    return render(request, 'bookchook/user_form.html', {'form': form})
