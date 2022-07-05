from django.shortcuts import get_object_or_404, render
from myapp.models import homepage_movies
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
movies_per_page = 12

def pagination(request, movie):
    page = request.GET.get('page', 1)
    paginator = Paginator(movie, movies_per_page)
    try:
        movie = paginator.page(page)
    except  PageNotAnInteger:
        movie = paginator.page(1)
    except EmptyPage:
        movie = paginator.page(paginator.num_pages)  
    return movie

def home(request, movie = None):
    if movie is None:
        movie = homepage_movies.objects.all()

    context = {
        'movie': pagination(request, movie)
    }

    return render(request,'index.html', context)
    
def movies(request):
    return render(request, 'details1.html')
         
def hollywood(request):
    moviehlwd = hollywood_movies.objects.all()
    return render(request,'hlwd.html', {'moviehlwd' : moviehlwd})

def about(request):
    return render(request, 'about.html')


def movie_detail(request, movie_id):
    movie = get_object_or_404(homepage_movies, pk=movie_id)

    context = {
        'movie' : movie
    }

    return render(request, 'details1.html', context)