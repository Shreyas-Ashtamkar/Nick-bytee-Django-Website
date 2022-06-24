from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('', views.home),
    path('Bollywood', views.bollywood , name = 'radio'),
    path('index', views.home, name = 'single'),
    path('hlwd', views.hollywood, name = 'hollywood'),
    path('Tollywood', views.tollywood, name = 'tollywood'),
    path('about', views.about, name = 'about'),
    path('details', views.details, name = 'details'),
    path('animes', views.animes, name = 'animes')
]