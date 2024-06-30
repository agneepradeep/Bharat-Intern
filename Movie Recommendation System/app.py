from flask import Flask, request, render_template, jsonify
import joblib
from dotenv import load_dotenv
import os
import pandas as pd
import requests

load_dotenv()

app = Flask(__name__)

# Load the models and data
tfidf = joblib.load('models/tfidf_vectorizer.joblib')
cosine_sim = joblib.load('models/cosine_similarity_matrix_tfidf.joblib')
count = joblib.load('models/count_vectorizer.joblib')
cosine_sim2 = joblib.load('models/cosine_similarity_matrix_count.joblib')
df2_cleaned = pd.read_csv('data/transformed_df2.csv')
q_movies = pd.read_csv('data/top_movies.csv')

OMDB_API_KEY = os.getenv('API_Key')

# Ensure indices are preserved
df2_cleaned = df2_cleaned.reset_index()
q_movies = q_movies.sort_values('score', ascending=False).head(15)  # Load top 15 movies and sort them

# Create a reverse map of indices and movie titles
indices = pd.Series(df2_cleaned.index, index=df2_cleaned['title']).drop_duplicates()

def get_recommendations(title, cosine_sim):
    # Ensure the title is properly capitalized
    title = title.title()
    
    # Get the index of the movie that matches the title
    idx = indices.get(title, None)
    if idx is None:
        return []

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return df2_cleaned['title'].iloc[movie_indices].tolist()

def fetch_movie_details(title):
    url = f'http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}'
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    top_movies = q_movies['title'].tolist()
    top_movies_details = [fetch_movie_details(title) for title in top_movies]
    return render_template('index.html', top_movies=top_movies_details)

@app.route('/recommend', methods=['GET'])
def recommend():
    movie_title = request.args.get('movie')
    filter_type = request.args.get('filter_type')

    if not movie_title or not filter_type:
        return jsonify({"error": "Missing movie title or filter type"}), 400

    try:
        # Ensure the movie title exists in your dataset
        if movie_title not in df2_cleaned['title'].values:
            return jsonify({"error": "Movie not found in dataset"}), 404

        # Get the index of the movie from the title
        idx = df2_cleaned[df2_cleaned['title'] == movie_title].index[0]

        # Use the appropriate similarity matrix based on the filter type
        if filter_type == 'plot':
            sim_scores = list(enumerate(cosine_sim[idx]))
        elif filter_type == 'actors_directors':
            sim_scores = list(enumerate(cosine_sim2[idx]))
        else:
            return jsonify({"error": "Invalid filter type"}), 400

        # Sort movies based on similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:16]  # Get top 15 similar movies

        recommendations = []
        for i, score in sim_scores:
            movie = df2_cleaned.iloc[i]
            # Fetch additional movie details from OMDB
            response = requests.get(f"http://www.omdbapi.com/?t={movie['title']}&apikey={OMDB_API_KEY}")
            movie_data = response.json()
            if movie_data['Response'] == 'True':
                recommendations.append({
                    'Title': movie_data['Title'],
                    'Poster': movie_data['Poster'],
                    'Plot': movie_data['Plot'],
                    'imdbRating': movie_data['imdbRating']
                })

        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
