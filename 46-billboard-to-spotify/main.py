import spotipy
import requests
import os


from dotenv import load_dotenv
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# Loads .env data into os.environ
load_dotenv()

# date = input(
#     "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
# )

#Scraping Billboard 100
response = requests.get(f"https://www.billboard.com/charts/hot-100/2000-08-26")
soup = BeautifulSoup(response.text, 'html.parser')
char_results = soup.find(name="div", class_="chart-results-list")

song_cards = char_results.select(
    selector=".o-chart-results-list-row-container > ul > li > ul > li:first-of-type"
    )

songs = []

for song_card in song_cards:
    song_title = song_card.find(name="h3", id="title-of-a-story").getText().strip()
    song_owner = song_card.find(name="span", class_="c-label").getText().strip()

    songs.append([song_owner, song_title])

#Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)
