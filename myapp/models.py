from distutils.command.upload import upload
from django.db import models

# Create your models here.
class homepage_movies(models.Model):
    logo = models.ImageField(upload_to = 'images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    download_link = models.CharField(max_length=100)
    category = models.CharField(max_length=30)
    rating = models.FloatField(max_length=2)
    quality = models.CharField(max_length=4)
    age = models.CharField(max_length=5)
    trailer = models.CharField(max_length=50)
    release_year = models.IntegerField()
    duration = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    @staticmethod
    def get_name():
        return 'movie'

class hollywood_movies(models.Model):
    logo = models.ImageField(upload_to = 'images')
    title = models.CharField(max_length=50)
    category = models.TextField()
    rating = models.FloatField(max_length=2)

