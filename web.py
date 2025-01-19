import streamlit as st
import pickle as pl

st.title('Movie Recommendation System')

movies= pl.load(open('movies.pkl','rb'))
movies_list= movies['title'].values
similarity= pl.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index= movies[movies['title']==movie].index[0]
    distance= similarity[movie_index]
    movies_indices= sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[1:6]

    recommended=[]
    for i in movies_indices:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

selected= st.selectbox('Select the movie',movies_list)

if st.button('Recommend'):
    recommendations= recommend(selected)
    for i in recommendations:
        st.write(i)