from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
     return render(request,'home.html')

def movies(request):
     return render(request,'movies.html')

def About(request):
     return render(request,'about.html')

def Features(request):
     return render(request,'features.html')

def AboutUs(request):
     return render(request,'aboutus.html')