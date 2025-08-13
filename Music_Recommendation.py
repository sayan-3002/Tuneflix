import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# -------------------
# Spotify API Keys (Replace with your regenerated ones)
# -------------------
SPOTIFY_CLIENT_ID = "98412d1c2e8b48b3983750ef76e8d536"
SPOTIFY_CLIENT_SECRET = "285257b8ed7243ab89817724cd85b605"

# Authenticate Spotify
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# -------------------
# Function to get songs based on mood + singer
# -------------------
def get_songs(mood, singer):
    query = mood
    if singer.strip():
        query += f" {singer}"
    results = sp.search(q=query, type="track", limit=20)  # Can be up to 50
    songs = []
    for track in results["tracks"]["items"]:
        songs.append({
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "url": track["external_urls"]["spotify"],
            "image": track["album"]["images"][0]["url"] if track["album"]["images"] else None
        })
    return songs

# -------------------
# Streamlit UI
# -------------------
st.set_page_config(page_title="🎵 AI Music Recommendation", layout="wide")
st.markdown(
    "<h1 style='text-align:center; color:#ff6600;'>🎵 AI Music Recommendation</h1>",
    unsafe_allow_html=True
)
st.write("<p style='color:white;'>Get music recommendations based on your mood and favorite singer.</p>",unsafe_allow_html=True)

# Mood options
moods = [
    "Happy", "Sad", "Romantic", "Party", "Chill", "Energetic",
    "Relax", "Focus", "Motivated", "Melancholy"
]
col1, col2 = st.columns(2)

with col1:
    mood_choice = st.selectbox("Select your mood", moods, index=0)
st.markdown("""
    <style>
    /* Target selectbox label text */
    div[data-testid="stSelectbox"] label {
        color: green;        /* Change text color */
        font-weight: bold;    /* Make it bold */
    }
    </style>
""", unsafe_allow_html=True)
with col2:
    singer_input = st.text_input("Enter singer's name (optional):", placeholder="e.g., Arijit Singh, Sonu Nigam, Shreya Ghosal")
st.markdown("""
    <style>
    /* Target the label of the second input column */
    div[data-testid="stTextInput"] label {
        color: green;        /* Change text color */
        font-weight: bold;    /* Optional bold */
    }
    </style>
""", unsafe_allow_html=True)

if st.button("🎧 Recommend Songs"):
    recommendations = get_songs(mood_choice, singer_input)
    if recommendations:
        st.markdown(
        f"<h3 style='color:yellow;'>Recommended Songs for Mood: '{mood_choice}'"
        + (f" & Singer: '{singer_input}'" if singer_input.strip() else "")
        + "</h3>",
    unsafe_allow_html=True
)
        cols = st.columns(5)
        for idx, song in enumerate(recommendations):
            with cols[idx % 5]:
                st.markdown(f"""
                    <div class="song-card">
                        <img src="{song['image']}" width="150"><br>
                        <div class="song-title">{song['name']}</div>
                        <div class="song-artist">{song['artist']}</div>
                        <a href="{song['url']}" target="_blank">🎵 Listen</a>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("No songs found for this mood/singer combination.")

# -------------------
# Custom CSS for Styling
# -------------------
st.markdown("""
    <style>
    /* ---------------- Page Styling ---------------- */
    /* Whole app background */
    .stApp {
        background-color: #04083b;  /* Dark blue page background */
    }

    /* Transparent main container so bg shows */
    [data-testid="stAppViewContainer"] .main .block-container {
        background: transparent;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] > div:first-child {
        background-color: #487cb5; /* Softer blue */
    }

    /* ---------------- Song Card Styling ---------------- */
    
    /* Card container for centering */
    .song-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Center all cards horizontally */
        row-gap: 40px; /* Vertical gap between rows */
        column-gap: 20px; /* Horizontal gap between columns */
        margin-top: 20px;
    }
    .song-card {
        background-color: #f0f0f5;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        width: 260px;
        height: 310px; /* Fixed card height */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }

    /* Song image styling */
    .song-card img {
        max-width: 100%;
        max-height: 150px;
        object-fit: contain;
        background-color: white;
        border-radius: 8px;
        padding: 8px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
    }

    /* Song title */
    .song-title {
        font-size: 16px;
        font-weight: bold;
        margin-top: 8px;
        color: #222222;
    }

    /* Artist name */
    .song-artist {
        font-size: 14px;
        color: #555555;
        margin-bottom: 8px;
    }

    /* Listen link */
    .listen-link {
        text-decoration: none;
        color: #1DB954; /* Spotify green */
        font-weight: bold;
        margin-top: auto;
    }
    .listen-link:hover {
        color: #14833b;
    }
    </style>
""", unsafe_allow_html=True)
