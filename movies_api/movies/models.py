from django.db import models


class Movies (models.Model):

    imdb_id = models.CharField(max_length=50) 
    title = models.CharField(max_length=100, null=True, blank=True)
    original_title = models.CharField(max_length=100, null=True, blank=True) 
    year = models.CharField(max_length=10, null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True) 
    duration = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    director = models.CharField(max_length=50, null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True)
    budget = models.CharField(max_length=50)
    reviews = models.FloatField(null=True, blank=True)
