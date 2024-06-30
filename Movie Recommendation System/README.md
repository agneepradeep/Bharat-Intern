# Movie Recommendation System

## Overview

This project focuses on building a movie recommendation system using a dataset from TMDB (The Movie Database). The system provides two types of recommendations:
1. **Demographic Filtering**: Recommends top movies based on score.
2. **Content-Based Filtering**: Recommends movies based on plot similarity or actor/director/keyword similarity.

The primary purpose of this system is to suggest movies that users might enjoy based on their preferences, enhancing their movie-watching experience.

## Model Architecture

The recommendation system consists of two main components:
1. **Demographic Filtering**: Uses a predefined score to recommend movies.
2. **Content-Based Filtering**:
   - **TF-IDF Vectorizer**: For vectorizing movie plots.
   - **Count Vectorizer**: For vectorizing actors, directors, and keywords.
   - **Cosine Similarity**: For calculating similarity between movies.

## Data Preprocessing

### Steps Taken:
1. **Data Cleaning**:
   - Removed null values.
   - Merged datasets on the movie ID to combine features like cast, crew, and title.
2. **Feature Engineering**:
   - Extracted important features such as cast, crew, keywords, and genres.
   - Converted stringified lists into Python lists using `literal_eval`.
3. **Normalization/Scaling**:
   - Applied vectorization using `CountVectorizer` and `TfidfVectorizer` to normalize text features.

## Model Training

### Training Process:
1. **Demographic Filtering**:
   - No training required.
   - Simply sorted movies based on a predefined score.
2. **Content-Based Filtering**:
   - Vectorized the movie plots and other features.
   - Calculated cosine similarity between movies.

### Hyperparameters:
- `CountVectorizer`: Default parameters.
- `TfidfVectorizer`: Default parameters.

### Training/Validation Split:
- Not applicable as it's an unsupervised approach.

## Model Evaluation

### Evaluation Metrics:
- **Precision and Recall**: Evaluated recommendations based on user feedback.
- **Cosine Similarity Score**: Used to measure similarity between movies.

### Test Data:
- Used a subset of the TMDB dataset for testing recommendations.

### Results and Analysis:
- The system effectively recommends movies based on plot and other features.
- Higher cosine similarity scores correlate with more relevant recommendations.

## Model Deployment

### Deployment Process:
1. **Environment**:
   - Flask application deployed on a web server.
2. **APIs/Endpoints**:
   - `/recommend`: Endpoint to get movie recommendations based on user input.
3. **Testing**:
   - Tested the deployment with different movie inputs to ensure accurate recommendations.

## Conclusion

The movie recommendation system provides accurate and relevant suggestions based on user preferences. The combination of demographic and content-based filtering enhances the recommendation quality, making it a robust solution for movie enthusiasts.

## References

- TMDB Movie Metadata: [Dataset Link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data)
- Scikit-learn Documentation
- Flask Documentation
- [Getting Started with a Movie Recommendation System - IBTESAM AHMED](https://www.kaggle.com/code/ibtesama/getting-started-with-a-movie-recommendation-system)

## Appendix

### Additional Information:
- Data preprocessing scripts.
- Sample API requests and responses.

### Dependencies:

- Python 3.8+
- Flask
- Pandas
- Numpy
- Scikit-learn
- Joblib
- Requests

### Installation:

```bash
pip install flask pandas numpy scikit-learn joblib requests
```

### How to Run:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```
2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the OMDB API key**:
    - Obtain an API key from [OMDB API](http://www.omdbapi.com/apikey.aspx).
    - Create a `.env` file in the root directory of the project and add your API key:
      ```sh
      OMDB_API_KEY=your_api_key_here
      ```

5. **Run the Flask app**:
   ```bash
   python app.py
   ```
6. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:5000/`.

By following these steps, you can set up and run the movie recommendation system locally. Enjoy exploring and finding new movies to watch!