import streamlit as st 
import pickle
import pandas as pd

import requests

def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey=15e148d7"
    data = requests.get(url).json()

    print(movie_title)
    print(data)

    if data.get("Response") == "True":
        poster = data.get("Poster")

        if poster and poster != "N/A":
            return poster

    return None
     

def recommend(movie):
    movie_index= movies[movies ['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies= []
    recommended_posters=[]
    for i in movies_list:
        movie_title= movies.iloc[i[0]].title


        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))

    return recommended_movies,recommended_posters

movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('Similarity.pkl','rb'))

st.title('Movie Recommender System') 

selected_movie= st.selectbox(
'Select the movie',
movies['title'].values)

if st.button('Recommend'):
    recommendations,posters= recommend(selected_movie)

    cols=st.columns(5)

    for i in range(len(recommendations)):
        with cols[i]:
            st.write(recommendations[i])

            # st.write(posters[i])

            if posters[i] and posters[i] != "N/A":

                st.image(posters[i])
            else:
                st.write("Poster Not Found")
        
     


     
