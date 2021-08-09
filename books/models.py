from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=120, null=True, blank=True)
    authors = models.CharField(max_length=120, blank=True, null=True)
    published_date = models.IntegerField(blank=True, null=True)
    categories = models.CharField(max_length=120, blank=True, null=True)
    average_rating = models.IntegerField(blank=True, null=True)
    ratings_count = models.IntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=200, blank=True, null=True)
    #TODO ADD ID FROM GOOGLE ex "id": "J6XAswEACAAJ",

    class Meta:
        unique_together=('title', 'authors')
