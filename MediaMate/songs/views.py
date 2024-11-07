from django.shortcuts import render
import pickle
similar=pickle.load(open('songs/pklfile_song/similar.pkl','rb'))
import numpy as np

# Create your views here.
def songs(request):
     if request.method == "POST":
          song_input = request.POST.get('song_input')
          # Ensure 'songs' is your dataframe, and 'song_input' is in the dataframe
          if song_input in songs['song'].values:
              index = songs[songs['song'] == song_input].index[0]
              distance = similar[index]  # Make sure this is a list/array of distances
              
              # Check if distance is subscriptable (i.e., a list or array)
              if isinstance(distance, (list, np.ndarray)):
                  song_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
                  
                  recommended_songs = []
                  for i in song_list:
                      recommended_songs.append(songs.iloc[i[0]]['song'])
                  
                  return render(request, 'songs.html', {'recommended_songs': recommended_songs})
              else:
                  error = "No valid distance data found"
                  return render(request, 'songs.html', {'error': error})
          else:
              error = "Song not found in the dataset"
              return render(request, 'songs.html', {'error': error})
     return render(request, 'songs.html')
