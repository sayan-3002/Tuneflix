
import streamlit as st
import pickle
import pandas as pd
import requests

# -------------------
# Load Data
# -------------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_df = pd.DataFrame(movies)

# -------------------
# Fetch Poster from TMDB API
# -------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=10df1df6d2b6c9c51ad6694563898891&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/150x225?text=No+Image"

# -------------------
# Recommend Movies
# -------------------
def recommend(movie):
    try:
        index = movies_df[movies_df['title'] == movie].index[0]
    except IndexError:
        return [], []

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_posters = []
    for i in distances:
        # Use ['id'] for movie_id, change if your column is different (e.g., 'movie_id')
        movie_id = movies_df.iloc[i[0]]['movie_id']
        recommended_movies.append(movies_df.iloc[i[0]]['title'])
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# -------------------
# Streamlit UI Setup
# -------------------
st.set_page_config(page_title="🎬 AI Movie Recommendation", layout="wide")

st.markdown(
    "<h1 style='text-align:center; color:#ff6600;'>🎬 AI Movie Recommendation</h1>",
    unsafe_allow_html=True
)
st.write(
    "<p style='color:white; text-align:center;'>Get curated movie recommendations similar to your favorite film.</p>",
    unsafe_allow_html=True
)

# Search form (same visual as your music recommender)
with st.form("recommendation_form"):
    selected_movie = st.selectbox(
        "🎥 Select or search for a movie",
        movies_df['title'].values
    )
    submitted = st.form_submit_button("🎯 Recommend Movies")
    st.markdown("""
    <style>
    /* Target selectbox label text */
    div[data-testid="stSelectbox"] label {
        color: green;        /* Change text color */
        font-weight: bold;    /* Make it bold */
    }
    </style>
""", unsafe_allow_html=True)

# -------------------
# Show Recommendations
# -------------------
if submitted:
    names, posters = recommend(selected_movie)
    if names:
        st.markdown(
            f"<h3 style='color:yellow;'>Movies similar to '{selected_movie}'</h3>",
            unsafe_allow_html=True
        )

        # Display in a 5-column grid like music UI
        cols = st.columns(5)
        for idx, (name, poster) in enumerate(zip(names, posters)):
            with cols[idx % 5]:
                st.markdown(f"""
                    <div class="movie-card">
                        <img src="{poster}" width="150">
                        <div class="movie-title">{name}</div>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("No recommendations found. Try another movie!")

# -------------------
# CSS Styling (music style!)
# -------------------
st.markdown("""
<style>
.stApp { background-color: #04083b; }
[data-testid="stAppViewContainer"] .main .block-container { background: transparent; }
[data-testid="stSidebar"] > div:first-child { background-color: #487cb5; }

.movie-card {
    background-color: #f0f0f5;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    width: 220px;
    min-height: 280px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.movie-card img {
    max-width: 110%;
    max-height: 180px;
    object-fit: contain;
    background-color: white;
    border-radius: 8px;
    padding: 4px;
}

.movie-title {
    font-size: 15px;
    font-weight: bold;
    margin-top: 8px;
    color: #222222;
}
</style>
""", unsafe_allow_html=True)

import streamlit as st
import pickle
import pandas as pd
import requests

# -------------------
# Load Data
# -------------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_df = pd.DataFrame(movies)

# -------------------
# Fetch Poster from TMDB API
# -------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=10df1df6d2b6c9c51ad6694563898891&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/150x225?text=No+Image"

# -------------------
# Recommend Movies
# -------------------
def recommend(movie):
    try:
        index = movies_df[movies_df['title'] == movie].index[0]
    except IndexError:
        return [], []

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_posters = []
    for i in distances:
        # Use ['id'] for movie_id, change if your column is different (e.g., 'movie_id')
        movie_id = movies_df.iloc[i[0]]['movie_id']
        recommended_movies.append(movies_df.iloc[i[0]]['title'])
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters

# -------------------
# Streamlit UI Setup
# -------------------
st.set_page_config(page_title="🎬 AI Movie Recommendation", layout="wide")

st.markdown(
    "<h1 style='text-align:center; color:#ff6600;'>🎬 AI Movie Recommendation</h1>",
    unsafe_allow_html=True
)
st.write(
    "<p style='color:white; text-align:center;'>Get curated movie recommendations similar to your favorite film.</p>",
    unsafe_allow_html=True
)

# Search form (same visual as your music recommender)
with st.form("recommendation_form"):
    selected_movie = st.selectbox(
        "🎥 Select or search for a movie",
        movies_df['title'].values
    )
    submitted = st.form_submit_button("🎯 Recommend Movies")
    st.markdown("""
    <style>
    /* Target selectbox label text */
    div[data-testid="stSelectbox"] label {
        color: green;        /* Change text color */
        font-weight: bold;    /* Make it bold */
    }
    </style>
""", unsafe_allow_html=True)

# -------------------
# Show Recommendations
# -------------------
if submitted:
    names, posters = recommend(selected_movie)
    if names:
        st.markdown(
            f"<h3 style='color:yellow;'>Movies similar to '{selected_movie}'</h3>",
            unsafe_allow_html=True
        )

        # Display in a 5-column grid like music UI
        cols = st.columns(5)
        for idx, (name, poster) in enumerate(zip(names, posters)):
            with cols[idx % 5]:
                st.markdown(f"""
                    <div class="movie-card">
                        <img src="{poster}" width="150">
                        <div class="movie-title">{name}</div>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("No recommendations found. Try another movie!")

# -------------------
# CSS Styling (music style!)
# -------------------
st.markdown("""
<style>
.stApp { background-color: #04083b; }
[data-testid="stAppViewContainer"] .main .block-container { background: transparent; }
[data-testid="stSidebar"] > div:first-child { background-color: #487cb5; }

.movie-card {
    background-color: #f0f0f5;
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    width: 220px;
    min-height: 280px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.movie-card img {
    max-width: 110%;
    max-height: 180px;
    object-fit: contain;
    background-color: white;
    border-radius: 8px;
    padding: 4px;
}

.movie-title {
    font-size: 15px;
    font-weight: bold;
    margin-top: 8px;
    color: #222222;
}
</style>
""", unsafe_allow_html=True)

