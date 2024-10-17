from django.shortcuts import render
import pickle 
import numpy as np
import pandas as pd


popular_df=pickle.load(open('books/pklfiles/popular.pkl','rb'))
pt=pickle.load(open('books/pklfiles/pt.pkl','rb'))
books=pickle.load(open('books/pklfiles/books.pkl','rb'))
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
        # Get the user input from the form
        user_input = request.POST.get('user_input')
        
        # Ensure 'pt' is a pandas DataFrame
        if isinstance(pt, pd.DataFrame):
            try:
                # index fetch
                index = np.where(pt.index == user_input)[0][0]
                similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]
            except IndexError:
                # Handle case where user_input doesn't exist in pt
                return render(request, 'book_recommend.html', {'error': "Book not found."})


            print(type(pt))             # This should be a pandas DataFrame or Series
            print(type(similarity_scores))   # This should be a numpy array or a list
            print(type(books))               # This should be a pandas DataFrame

            data = []
            for i in similar_items:
                item = []
                temp_df = books[books['Book-Title'] == pt.index[i[0]]]
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
                item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
                
                data.append(item)

            # Pass the recommended books to the template
            return render(request, 'book_recommend.html', {'data': data, 'user_input': user_input})
        else:
            return render(request, 'book_recommend.html', {'error': "Data format error."})
    
    # In case of GET request
    return render(request, 'book_recommend.html')

