from django.contrib import admin
from django.urls import path
from books.views import BooksViewSet, BooksDetailSet, DownloadBooksFromApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BooksViewSet.as_view()),
    path('books/<int:pk>', BooksDetailSet.as_view()),
    path('get-data/<str:q>', DownloadBooksFromApi),
]
