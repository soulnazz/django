from django.contrib import admin
# В файле book/admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)

# Register your models here.
