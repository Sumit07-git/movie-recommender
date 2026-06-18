# 🎬 Movie Recommender System

A content-based movie recommendation system built using Python, Machine Learning, and Streamlit. The application recommends movies similar to a selected movie and displays their posters using the OMDb API.

## 🚀 Features

* Recommend 5 similar movies based on content similarity.
* Interactive web interface built with Streamlit.
* Movie posters fetched dynamically using the OMDb API.
* Fast recommendations using precomputed cosine similarity.

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit
* Pickle
* OMDb API

## 📂 Dataset

This project uses the TMDB 5000 Movie Dataset:

* tmdb_5000_movies.csv
* tmdb_5000_credits.csv

## 📊 Working

1. Movie and credits datasets are merged.
2. Important features such as genres, keywords, cast, crew, and overview are extracted.
3. Text data is combined into tags.
4. CountVectorizer converts text into vectors.
5. Cosine Similarity is used to find similar movies.
6. Streamlit provides an interactive user interface.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
movie-recommender/
│
├── app.py
├── movie.py
├── vectorization.py
├── movies.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── README.md
└── requirements.txt
```

## 🔮 Future Improvements

* Deploy the application online.
* Use TMDB API for more accurate posters.
* Add movie ratings and trailers.
* Improve recommendation quality using advanced NLP techniques.

## 👨‍💻 Author

**Sumit Samal**
