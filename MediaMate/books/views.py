from django.shortcuts import render
import pickle 
popular_df=pickle.load(open('books/pklfiles/popular.pkl','rb'))

# Create your views here.
def books(request):
    # Create a list of dictionaries to hold book data
    books_data = []
    for i in range(len(popular_df)):
        books_data.append({
            'name': popular_df['Book-Title'].values[i],
            'author': popular_df['Book-Author'].values[i],
            'image': popular_df['Image-URL-M'].values[i],
            'votes': popular_df['num_ratings'].values[i],
            'rating': popular_df['avg_rating'].values[i],
        })
    
    return render(request, 'books.html', {'books': books_data})

