from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd
# Create your views here.




def home(request):
     return render(request,'home.html')

def movies(request):
     movies_dict=pickle.load(open('movies/pklfile_movie/movies_dict.pkl','rb'))
     movies=pd.DataFrame(movies_dict)
     movie_titles=movies['title'].values


     if request.method == 'POST':
        # Get the user input from the form
        user_input = request.POST.get('movie_input')

        
     return render(request, 'movies.html', {'movie_titles': movie_titles})

def About(request):
     return render(request,'about.html')

def Features(request):
     return render(request,'features.html')

def AboutUs(request):
     return render(request,'aboutus.html')