from movie import preprocess
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

new_df=preprocess()


cv= CountVectorizer(max_features=5000,stop_words='english')

vectors=cv.fit_transform(new_df['tags']).toarray()

similarity=cosine_similarity(vectors)

def recommend(movie):
    movie_index= new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)


pickle.dump(new_df.to_dict(),open('movies.pkl','wb'))
pickle.dump(similarity,open('Similarity.pkl','wb'))













