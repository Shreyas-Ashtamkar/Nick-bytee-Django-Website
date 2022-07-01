from django.shortcuts import render
from myapp.models import homepage_movies
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *


# Create your views here.
def home(request):
    movie = homepage_movies.objects.all() 
    return render(request,'index.html', {'movie' : movie})
    
def movies(request):
    return render(request, 'details1.html')
         
def hollywood(request):
    moviehlwd = hollywood_movies.objects.all()
    return render(request,'hlwd.html', {'moviehlwd' : moviehlwd})
    