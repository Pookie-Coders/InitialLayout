import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dummy movie dataset
movies = pd.DataFrame([
    {"id": 1, "title": "Inception", "genres": "Sci-Fi Thriller"},
    {"id": 2, "title": "Interstellar", "genres": "Sci-Fi Drama"},
    {"id": 3, "title": "The Dark Knight", "genres": "Action Thriller"},
    {"id": 4, "title": "Titanic", "genres": "Romance Drama"},
    {"id": 5, "title": "Avengers: Endgame", "genres": "Action Sci-Fi"},
])

# Convert genres into TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(movies["genres"])

def get_recommendations(liked_movie_title):
    """Finds similar movies based on a liked movie using TF-IDF + Cosine Similarity."""
    if liked_movie_title not in movies["title"].values:
        return ["Movie not found in dataset"]

    # Get index of the liked movie
    movie_index = movies[movies["title"] == liked_movie_title].index[0]

    # Compute cosine similarity scores
    similarity_scores = cosine_similarity(tfidf_matrix[movie_index], tfidf_matrix).flatten()

    # Get top 3 similar movies (excluding the liked one)
    recommended_indices = similarity_scores.argsort()[-4:-1][::-1]
    recommended_movies = movies.iloc[recommended_indices]["title"].tolist()

    return recommended_movies
