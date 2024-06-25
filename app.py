import streamlit as st
import pickle
import pandas as pd
import requests 
from dotenv import load_dotenv
import os
load_dotenv()

apiKey= os.getenv('API_KEY')

def fetch_poster(movieId):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US'.format(movieId,apiKey))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500'+ data['poster_path']


def recommend(movie):
    movieIdx=movies[movies['title']==movie].index[0]
    dist=similarity[movieIdx]
    movies_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:7]
    posters=[]

    recommended_movies=[]
    for i in movies_list:
        movieId = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movieId))

    return recommended_movies, posters

movies_dict=pickle.load(open('pickle/movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('pickle/similarity.pkl','rb'))
st.title('Movie Recommender')

movie_name=st.selectbox('Enter a movie',movies['title'].values)

if st.button('Recommend'):
    names, posters=recommend(movie_name)
    row1 = st.columns(3)
    row2 = st.columns(3)
    idx=0
    for col in row1 + row2:
        tile = col.container(height=390)
        tile.write(names[idx])
        tile.image(posters[idx])
        idx+=1


    