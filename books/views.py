from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer, BookFullSerializer


class BooksViewSet(APIView):

    def get(self, *args, **kwargs):
        books = Book.objects.all()
        serializer = (BookSerializer(books, many=True))
        return Response(serializer.data, status=status.HTTP_200_OK)


class BooksDetailSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = BookFullSerializer
