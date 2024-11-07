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
        book_name = request.POST.get('user_input')
        
        # Debug pt type
        print(f"pt type: {type(pt)}")

        if isinstance(pt, (pd.DataFrame, pd.Series)):
            # Ensure pt.index is accessible
            try:
                index = np.where(pt.index == book_name)[0][0]
            except IndexError:
                return render(request, 'book_recommend.html', {'error': 'Book not found.'})
        else:
            return render(request, 'book_recommend.html', {'error': 'Pivot table (pt) is not defined properly.'})

        # Proceed with the rest of the recommendation logic
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]
        
        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            
            data.append(item)
        
        return render(request, 'book_recommend.html', {'data': data})
    
    return render(request, 'book_recommend.html')


