from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from .filters import CustomSearchFilter
from .models import Book


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

def DownloadBooksFromApi(request, q):
    c = connector.APIConnector(q=q)
    c.get_book_data()
    return HttpResponse(f'<h1>Parameter is {q}</h1>')

