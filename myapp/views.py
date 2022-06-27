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

class ReactView(APIView):
    
    serializer_class = ReactSerializer
  
    def get(self, request):
        detail = [ {"detail": detail.title, "description" : detail.description, "links" : detail.links, "type1" : detail.type1,
        "type2" : detail.type2, "rating" : detail.rating, "quality" : detail.quality} 
        for detail in homepage_movies.objects.all()]
        return Response(detail)
  
    def post(self, request):
  
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)



"""def hollywood(request):
    return render(request,'hlwd.html')

def bollywood(request):
    return render(request, 'blwd.html')

def catalog2(request):
    return render(request, 'catalog2.html')

def tollywood(request):
    return render(request, 'details1.html')

def animes(request):
    return render(request, 'blwd.html')

def about(request):
    return render(request, 'about.html')

def details(request):
    return render(request, 'details2.html')"""