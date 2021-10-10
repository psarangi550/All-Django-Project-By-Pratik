from django.db import models

# Create your models here.
class Movie(models.Model):#creating the Models class called movies
    relese_date=models.DateTimeField(verbose_name="Movie Relese Date")
    movie_name=models.CharField(max_length=100)
    hero=models.CharField(max_length=100)
    heroine=models.CharField(max_length=100)
    director=models.CharField(max_length=100)
    rating=models.IntegerField()

