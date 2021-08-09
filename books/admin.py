from django.contrib import admin
from .models import Book


class AdminBookView(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Book, AdminBookView)
