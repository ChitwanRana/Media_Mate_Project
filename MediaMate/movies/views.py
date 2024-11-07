from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd
# Create your views here.




def home(request):
     return render(request,'home.html')

def movies(request):
    movies_dict = pickle.load(open('movies/pklfile_movie/movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    movie_titles = movies['title'].values
    similar = pickle.load(open('movies/pklfile_movie/similar.pkl', 'rb'))

    recommended_movies = []  # Initialize an empty list for recommended movies

    if request.method == 'POST':
        # Get the user input from the form
        user_input = request.POST.get('movie_input')

        index = movies[movies['title'] == user_input].index[0]
        distance = similar[index]
        movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        for i in movies_list:
            recommended_movies.append(movies.iloc[i[0]]['title'])

    return render(request, 'movies.html', {'movie_titles': movie_titles, 'recommended_movies': recommended_movies})


def About(request):
     return render(request,'about.html')

def Features(request):
     return render(request,'features.html')

def AboutUs(request):
     return render(request,'aboutus.html')