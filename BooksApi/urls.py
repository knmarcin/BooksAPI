from django.contrib import admin
from django.urls import path
from books.views import BooksViewSet, BooksDetailSet, download_books_from_api

urlpatterns = [
    path('books/', BooksViewSet.as_view()),
    path('books/<int:pk>', BooksDetailSet.as_view()),
    path('db/', download_books_from_api),
]
