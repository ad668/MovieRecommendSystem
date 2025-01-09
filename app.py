import streamlit as st
import pickle
import pandas as pd




def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommeded_movies=[]
    for i in movies_list:

        recommeded_movies.append(movies.iloc[i[0]].title)
    return recommeded_movies

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


st.title("Movie Remmondation System")

Selected_movie_name=st.selectbox(
    'Which movie you want to see..',
    movies['title'].values
)

if st.button('Recommend'):
    recommendation=recommend(Selected_movie_name)
    for i in recommendation:
        st.write(i)
    # st.write(Selected_movie_name)