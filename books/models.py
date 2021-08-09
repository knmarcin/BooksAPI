from django.db import models


class Book(models.Model):
    google_id = models.CharField(max_length=40, unique=True)
    title = models.CharField(max_length=120, null=True, blank=True)
    authors = models.CharField(max_length=120, blank=True, null=True)
    published_date = models.IntegerField(blank=True, null=True)
    categories = models.CharField(max_length=120, blank=True, null=True)
    average_rating = models.IntegerField(blank=True, null=True)
    ratings_count = models.IntegerField(blank=True, null=True)
    thumbnail = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['-id']
