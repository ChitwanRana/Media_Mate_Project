from django.shortcuts import render
import pickle
similar=pickle.load(open('songs/pklfile_song/similar.pkl','rb'))
songs_df=pickle.load(open('songs/pklfile_song/songs.pkl','rb'))
import numpy as np

# Create your views here.
import numpy as np
from django.shortcuts import render

# Assuming 'songs_df' is your DataFrame containing song data
def songs(request):  # Renamed the view function to avoid conflicts
    if request.method == "POST":
        song_input = request.POST.get('song_input')
        
        # Ensure 'songs_df' is your DataFrame and 'song_input' is in the DataFrame
        if song_input in songs_df['song'].values:
            index = songs_df[songs_df['song'] == song_input].index[0]
            distance = similar[index]  # Ensure this is a list/array of distances
            
            # Check if distance is subscriptable (i.e., a list or array)
            if isinstance(distance, (list, np.ndarray)):
                # Generate a sorted list of recommended songs
                song_list = sorted(enumerate(distance), key=lambda x: x[1])[:5]  # Get top 5
                
                recommended_songs = [songs_df.iloc[i[0]]['song'] for i in song_list]

                return render(request, 'songs.html', {'recommended_songs': recommended_songs})
            else:
                error = "No valid distance data found"
                return render(request, 'songs.html', {'error': error})
        else:
            error = "Sorry Song not found in the dataset , Check Spelling or Case Senstivity"
            return render(request, 'songs.html', {'error': error})
    
    return render(request, 'songs.html')
