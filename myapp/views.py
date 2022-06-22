from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def catalog1(request):
    return render(request,'catalog1.html')

def catalog2(request):
    return render(request, 'catalog2.html')