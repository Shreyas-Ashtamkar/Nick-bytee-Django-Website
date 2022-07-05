from django.urls import path, include
from . import views

app_name = 'movie'

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('', views.home),
    path('hlwd', views.hollywood, name = 'hollywood'),
    path('about', views.about, name = 'about'),
    path('<int:movie_id>', views.movie_detail, name='movie-detail')

    ]