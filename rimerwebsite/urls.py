"""rimerweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('songs', views.songs, name='songs'),
    path('albums', views.albums, name='albums'),
    path('search_albums',views.search_albums,name="search_albums"),
    path('search_songs',views.search_songs,name="search_songs"),
    path('search_poems',views.search_poems,name="search_poems"),
    path('contact', views.contact, name='contact'),
    path('poems', views.poems, name="poems"),
    path('about', views.about, name="about"),
  
]
