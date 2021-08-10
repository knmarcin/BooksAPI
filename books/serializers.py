from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'authors', 'title', 'published_date')


class BookFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',
                  'authors',
                  'published_date',
                  'categories',
                  'average_rating',
                  'ratings_count',
                  'thumbnail')


class GetBookSerializer(serializers.Serializer):
        question = serializers.CharField(max_length=40)