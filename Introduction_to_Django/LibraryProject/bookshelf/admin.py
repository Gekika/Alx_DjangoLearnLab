from django.contrib import admin
from .models import Book

# Customizing the Admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # columns to display in the list view
    search_fields = ('title', 'author')                      # enable search by title and author
    list_filter = ('publication_year',)                      # add a filter by publication year

# Register the Book model with custom admin settings
admin.site.register(Book, BookAdmin)
