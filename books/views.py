from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CustomSearchFilter
from django.shortcuts import redirect

from .models import Book
from .serializers import BookSerializer, BookFullSerializer
from utils import connector


class BooksViewSet(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, CustomSearchFilter, filters.OrderingFilter]
    filterset_fields = ['published_date']
    search_fields = ['authors']
    ordering_fields = ['published_date']


class BooksDetailSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = BookFullSerializer


def download_books_from_api(request, q):
    c = connector.APIConnector(q=q)
    c.get_book_data()
    return redirect('/books/')
