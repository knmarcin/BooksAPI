from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','authors', 'title', 'published_date',)

class BookFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id',
                  'title',
                  'authors',
                  'published_date',
                  'categories',
                  'average_rating',
                  'ratings_count',
                  'thumbnail')