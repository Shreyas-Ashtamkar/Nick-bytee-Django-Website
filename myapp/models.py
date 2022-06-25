from distutils.command.upload import upload
from django.db import models

# Create your models here.
class homepage_movies(models.Model):
    logo = models.ImageField(upload_to = 'images')
    title = models.CharField(max_length=100)
    description = models.TextField()
    links = models.TextField()
    type1 = models.TextField()
    type2 = models.TextField()
    rating = models.FloatField(max_length=2)
    quality = models.TextField()
    age = models.TextField()
    new = models.BooleanField(default=False)