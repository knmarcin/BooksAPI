from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CustomSearchFilter

from .models import Book
from .serializers import BookSerializer, BookFullSerializer


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
