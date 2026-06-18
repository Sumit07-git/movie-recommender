import numpy as np 
import pandas as pd 
import ast
import nltk
from nltk.stem.porter import PorterStemmer

ps=PorterStemmer()

def preprocess():
    mov=pd.read_csv('tmdb_5000_movies.csv')
    credit=pd.read_csv('tmdb_5000_credits.csv')

    mov=mov.merge(credit,on='title')

    mov=mov[['movie_id','title','overview','genres','keywords','cast','crew']]

    mov.dropna(inplace=True)

   

    def convert(obj):
        L=[]
        for i in ast.literal_eval(obj):
            L.append(i['name'])
        return L

    mov['genres']=mov['genres'].apply(convert)
    mov['keywords']=mov['keywords'].apply(convert)

    def convert3(obj):
        L=[]
        counter=0
        for i in ast.literal_eval(obj):
            if counter != 3:

                L.append(i['name'])
                counter+=1
            else:
                break
        return L

    mov['cast']=mov['cast'].apply(convert3)


    def fetch_dir(obj):
        L=[]
        for i in ast.literal_eval(obj):
            if i['job']=='Director':
                L.append(i['name'])
                break
        return L

   

    mov['crew']=mov['crew'].apply(fetch_dir)

    

    mov['overview']=mov['overview'].apply(lambda x:x.split()) 

    mov['genres']=mov['genres'].apply(lambda x:[i.replace(" ","")for i in x])
    mov['keywords']=mov['keywords'].apply(lambda x:[i.replace(" ","")for i in x])
    mov['cast']=mov['cast'].apply(lambda x:[i.replace(" ","")for i in x])
    mov['crew']=mov['crew'].apply(lambda x:[i.replace(" ","")for i in x])

    mov['tags']= mov['overview']+ mov['genres']+ mov['keywords']+ mov['cast']+ mov['crew']

    new_df=mov[['movie_id','title','tags']].copy()

    new_df['tags']=new_df['tags'].apply(lambda x:" ".join(x))

    new_df['tags']=new_df['tags'].apply(lambda x:x.lower())

    def stem(text):
        y =[]

        for i in text.split():
            y.append(ps.stem(i))

        return " ".join(y)

    new_df['tags']=new_df['tags'].apply(stem)

    return new_df

 






 

 
