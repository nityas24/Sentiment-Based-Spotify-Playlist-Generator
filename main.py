import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, render_template

# Spotify API credentials
SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = "http://localhost:9000"

# Authenticate
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-public"))

app = Flask(__name__)

# Get current user's details
user = sp.current_user()
print(f"Authenticated as: {user['display_name']}")

# Home page (Form for user input)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_text = request.form["journal"]
        print(f"User input: {user_text}")
        
        # Placeholder: Process sentiment and fetch songs
        message = f"Journal Entry Received: {user_text}"
        return render_template("index.html", message=message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=9000, debug=True)
