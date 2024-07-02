import streamlit as st
import pandas as pd
import joblib
import requests

# Load environment variables
OMDB_API_KEY = st.secrets['API_Key']

# Load the models and data
cosine_sim = joblib.load('models/cosine_similarity_matrix_tfidf.joblib')
cosine_sim2 = joblib.load('models/cosine_similarity_matrix_count.joblib')
df2_cleaned = pd.read_csv('data/transformed_df2.csv')
q_movies = pd.read_csv('data/top_movies.csv')

# Ensure indices are preserved
df2_cleaned = df2_cleaned.reset_index()
q_movies = q_movies.sort_values('score', ascending=False).head(15)  # Load top 15 movies and sort them

# Create a reverse map of indices and movie titles
indices = pd.Series(df2_cleaned.index, index=df2_cleaned['title']).drop_duplicates()

def get_recommendations(title, cosine_sim):
    title = title.title()
    idx = indices.get(title, None)
    if idx is None:
        return []

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df2_cleaned['title'].iloc[movie_indices].tolist()

def fetch_movie_details(title):
    url = f'http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}'
    response = requests.get(url)
    return response.json()

def create_movie_card(movie_details):
    if movie_details['Response'] == 'True':
        card = f"""
        <div class="movie-card">
            <img src="{movie_details['Poster']}" alt="{movie_details['Title']} poster">
            <p style = "text-align: center; font-size: 20px; font-weight: bolder">{movie_details['Title']}</p>
            <p style = "text-align: left;">{movie_details['Plot']}</p>
            <p><strong>IMDB Rating:</strong> {movie_details['imdbRating']}</p>
        </div>
        """
        return card
    return ""

# Custom CSS styles
movie_card_css = """
<style>
    .movie-card {
        display: inline-block;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 15px;
        margin: 15px;
        text-align: center;
        background-color: #fff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
        width: 320px;
        height: 400px;
        overflow:auto;
    }
    .movie-card:hover {
        transform: scale(1.05);
    }
    .movie-card img {
        max-width: 50%;
        height: auto;
        border-radius: 5px;
    }
</style>
"""

# Streamlit App
st.title("Movie Media")

# Inject custom CSS styles
st.markdown(movie_card_css, unsafe_allow_html=True)

menu = ["Trending", "Search"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Trending":
    st.subheader("Top 15 Movies")
    movie_cards = ""
    for index, row in q_movies.iterrows():
        movie_details = fetch_movie_details(row['title'])
        movie_cards += create_movie_card(movie_details)
    st.markdown(movie_cards, unsafe_allow_html=True)

elif choice == "Search":
    st.subheader("Search Movie Recommendations")
    movie_name = st.text_input("Enter movie name")
    filter_type = st.radio("Filter Type", ("plot", "actors_directors"))

    if st.button("Search"):
        if movie_name:
            if filter_type == "plot":
                recommendations = get_recommendations(movie_name, cosine_sim)
            else:
                recommendations = get_recommendations(movie_name, cosine_sim2)
            
            if recommendations == []:
                st.markdown("Not available in our database")
            else:
                st.subheader("Recommended Movies:")
                movie_cards = ""
                for title in recommendations:
                    movie_details = fetch_movie_details(title)
                    movie_cards += create_movie_card(movie_details)
                st.markdown(movie_cards, unsafe_allow_html=True)
        else:
            st.error("Please enter a movie name.")
