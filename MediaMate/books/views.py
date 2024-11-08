from django.shortcuts import render
import pickle 
import numpy as np
import pandas as pd


popular_df=pickle.load(open('books/pklfiles/popular.pkl','rb'))
pt=pickle.load(open('books/pklfiles/pt.pkl','rb'))
books_data = pickle.load(open('books/pklfiles/books.pkl', 'rb'))
similarity_scores=pickle.load(open('books/pklfiles/similarity_scores.pkl','rb'))

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

def recommend(request):
    if request.method == 'POST':
        book_name = request.POST.get('user_input')

        try:
            # Assuming pt is defined somewhere in your code
            index = np.where(pt.index == book_name)[0][0]  # Find the index of the book
        except IndexError:
            return render(request, 'book_recommend.html', {'error': 'Book not found'})

        # Ensure similarity_scores is defined and valid
        try:
            similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
        except IndexError:
            return render(request, 'book_recommend.html', {'error': 'Invalid index for similarity scores'})

        data = []
        for i in similar_items:
            item = []
            temp_df = books_data[books_data['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)

        return render(request, 'book_recommend.html', {'data': data})

    return render(request, 'book_recommend.html')