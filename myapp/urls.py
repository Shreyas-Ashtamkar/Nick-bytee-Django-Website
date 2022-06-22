from django.urls import path, include

from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('',views.home),
    path('catalog1', views.catalog1 , name = 'radio'),
    path('index', views.home, name = 'single'),
    path('catalog2', views.catalog2, name = 'catalog2')
]