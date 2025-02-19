from flask import Flask, request, render_template
from transformers import pipeline
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize Flask app
app = Flask(__name__)

# Initialize Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Spotify API credentials
SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = "http://localhost:9000"

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-public"))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form["journal"]
        
        # Analyze sentiment
        sentiment_result = sentiment_pipeline(user_text)
        sentiment_label = sentiment_result[0]['label']  # 'POSITIVE' or 'NEGATIVE'
        
        # Debugging
        print(f"User input: {user_text}")
        print(f"Sentiment: {sentiment_label}")

        # Generate playlist based on sentiment
        playlist_name = f"Mood Playlist - {sentiment_label}"
        playlist = sp.user_playlist_create(sp.current_user()["id"], playlist_name, public=True)
        
        return render_template("index.html", message=f"Playlist '{playlist_name}' created!")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=9000, debug=True)

