"""
URL configuration for MediaMate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from movies.views import *
from books.views import *
from movies.views import *
from songs.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('books/',books,name='books'),
    path('movies/',movies,name='movies'),
    path('songs/',songs,name='songs'),
    path('About/',About,name='About'),
    path('features/',Features,name='features'),
    path('aboutus/',AboutUs,name='aboutus'),
    path('recommend/', recommend, name='recommend'),
    # path('book_recommend/', book_recommend, name='book_recommend'),
]
