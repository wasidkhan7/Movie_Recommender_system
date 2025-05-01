import streamlit as st
import pandas as pd
import pickle
import requests


# Load movie data and similarity matrix
movies_df = pickle.load(open("movies.pkl", "rb"))  # DataFrame with movie details
similarity = pickle.load(open("similarity.pkl", "rb"))  # 2D similarity matrix

# Extract movie titles
movies_title = movies_df['title'].values

# Streamlit UI
st.title(" Movie Recommender System")

# Dropdown to select a movie
selected_movie = st.selectbox('Would you like any movie recommendations?', movies_title)



# Setting posters to movie titles


def fetch_poster(movie_id):
    api_key = "bc1d8fc0d66dcba02bb1cbb7a0a3cc7f"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    full_path = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else ""
    return full_path



# Recommendation logic( same Function which we used in model building)
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies_df.iloc[i[0]]['id']
        recommended_titles.append(movies_df.iloc[i[0]]['title'])
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_titles, recommended_posters



# Button to get recommendations
if st.button('Recommend'):
    titles, posters = recommend(selected_movie)
    st.subheader("Top 5 Recommended Movies:")

  
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(titles[0])
        st.image(posters[0])
  
    with col2:
        st.text(titles[1])
        st.image(posters[1])  

    with col3:
        st.text(titles[2])
        st.image(posters[2])
  
    with col4:
        st.text(titles[3])
        st.image(posters[3])

    with col5:
        st.text(titles[4])
        st.image(posters[4])
  
