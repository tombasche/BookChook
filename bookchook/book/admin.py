from django.contrib import admin

from bookchook.book.google_books import GoogleBook
from .models import Book, Series, ISBNBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'series', 'status', 'location')

    def save_model(self, request, obj, form, change):
        obj.user = request.user

        if obj.isbn is not None:
            google_book = GoogleBook(obj.isbn)

        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        return 'isbn', 'name', 'author', 'status', 'series', 'number', 'location', 'comment'

    def get_queryset(self, request):
        return Book.objects.filter(user=request.user)


@admin.register(ISBNBook)
class ISBNBookAdmin(admin.ModelAdmin):
    # list_display = ('name', 'author', 'series', 'status', 'location')

    def save_model(self, request, obj, form, change):
        obj.user = request.user.username
        google_book = GoogleBook(obj.isbn)

        obj.name = google_book.title
        obj.author = google_book.author
        obj.comment = google_book.description

        super().save_model(request, obj, form, change)

    # def get_fields(self, request, obj=None):
    #     return 'isbn', 'name', 'author', 'status', 'series', 'number', 'location', 'comment'
    #
    # def get_queryset(self, request):
    #     return Book.objects.filter(user=request.user)



@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_fields(self, request, obj=None):
        return 'name',

    def get_queryset(self, request):
        return Series.objects.filter(user=request.user)
