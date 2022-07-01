from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('', views.home),
    path('batman', views.movies, name = 'Movie_Details'),
    path('hlwd', views.hollywood, name = 'hollywood')

    ]