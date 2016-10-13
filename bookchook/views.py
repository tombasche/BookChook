from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Book
from .forms import BookForm

def book_list(request):
    books = Book.objects.all
    return render(request, 'bookchook/book_list.html', {'books': books})

def book_search(request):
    if request.method == "GET":
        search_query = request.GET.get('search_box', None)
        if search_query is not None:
            books = Book.objects.filter(name__icontains=search_query)
        else:
            return render(request, 'bookchook/book_search.html', {})
    return render(request, 'bookchook/book_list.html', {'books': books})


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            books = Book.objects.all
            return render(request, 'bookchook/book_list.html', {'books': books})
    else:
        form = BookForm()
    return render(request, 'bookchook/book_form.html', {'form': form})
