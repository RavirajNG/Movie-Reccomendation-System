import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6956ef3976bb94e25a03eb2849e71011&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommended_movies_name.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies_name, recommended_movies_poster

st.header('Moviehub4U')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie = st.selectbox(
"Search MovieHUb",
movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])