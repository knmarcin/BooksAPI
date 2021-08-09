from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    published_date = models.IntegerField()
    categories = models.CharField(max_length=120)
    average_rating = models.IntegerField()
    ratings_count = models.IntegerField()
    thumbnail = models.CharField(max_length=200)