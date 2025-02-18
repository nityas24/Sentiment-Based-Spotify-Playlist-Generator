import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
SPOTIPY_CLIENT_ID = "01f719311080477ba6ae8af40945451b"
SPOTIPY_CLIENT_SECRET = "553bbd7bee3e4176b928e803cfdbdb00"
SPOTIPY_REDIRECT_URI = "http://localhost:9000"

# Authenticate
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-public"))
sp.current_user()  # Get the current user's details.
