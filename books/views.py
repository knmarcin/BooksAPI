from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

from utils import connector

#TODO Relative imports are not a good idea
from .filters import CustomSearchFilter
from .models import Book
from .serializers import BookSerializer, BookFullSerializer, GetBookSerializer


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


@api_view(['POST'])
def download_books_from_api(request, *args, **kwargs):
    q = GetBookSerializer(data=request.data)
    print(q)
    if q.is_valid():
        c = connector.APIConnector(q=q.data.get('q'))
        c.get_book_data()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
