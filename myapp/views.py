from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def hollywood(request):
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
    return render(request, 'details2.html')