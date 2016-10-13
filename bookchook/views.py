from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect
from django.db.models import Q
from django.core.exceptions import ValidationError
from .models import Book
from .forms import BookForm

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
            books = Book.objects.filter(name__icontains=search_query, user=request.user)
            return render(request, 'bookchook/book_list.html', {'books': books})
        else:
            return render(request, 'bookchook/book_search.html', {})
    books = Book.objects.filter(user=request.user)
    return render(request, 'bookchook/book_list.html', {'books': books})

@login_required
def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            existingBook = Book.objects.filter(name__icontains=book.name, user=request.user)
            if not existingBook:
                book.user = request.user
                book.save()
                books = Book.objects.filter(user=request.user)
                return render(request, 'bookchook/book_list.html', {'books': books})
            else:
                form = BookForm()
                messages.error(request, "This book already exists!")
                return render(request, 'bookchook/book_form.html', {'form': form})
    else:
        form = BookForm()
        messages.error(request,None)
    return render(request, 'bookchook/book_form.html', {'form': form})
