from django.contrib import admin
from .models import Book, Series

admin.site.register(Series)
admin.site.index_title = 'BookChook'
admin.site.site_header = 'BookChook'
admin.site.index_title = 'BookChook'
admin.site.site_title = 'Main'


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
