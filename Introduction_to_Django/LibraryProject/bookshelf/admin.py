from django.contrib import admin

# Register your models here.
from .models import Book   # <-- use the actual model name

admin.site.register(Book)
