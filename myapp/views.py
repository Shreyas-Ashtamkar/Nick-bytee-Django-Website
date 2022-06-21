from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def radio(request):
    return render(request, 'radio1.html')