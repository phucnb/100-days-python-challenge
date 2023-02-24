from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
import os
import json

SP_ID = os.environ.get('SPOTIFY_ID')
SP_KEY = os.environ.get('SPOTIFY_KEY')

BB_URL = 'https://www.billboard.com/charts/hot-100/'

date = input("Enter the date you want to check the billboard (YYYY-MM-DD): ")
html = requests.get(f'{BB_URL}/{date}')

soup = BeautifulSoup(html.text, 'html.parser')
songs_tag = soup.find_all(name='ul', class_='o-chart-results-list-row')
billboard = []
for song in songs_tag:
    song_rank = song.find(name='span', class_='c-label').getText().strip()
    song_name = song.find(name='h3', class_='c-title').getText().strip()
    song_singer = song.find(name='li', class_='lrv-u-width-100p').find(name='span', class_='c-label').getText().strip()
    billboard.append({'name' : song_name, 'artist' : song_singer.replace(' &', ',')})



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SP_ID,
                                               client_secret=SP_KEY,
                                               redirect_uri="http://example.com",
                                               scope="user-library-read playlist-modify-private playlist-modify-public"))

tracks_list = []
for song in billboard:
    results = sp.search(q=f"track:{song['name']} artist:{song['artist']}", limit=1, type='track')
    try:
        track_id = results['tracks']['items'][0]['uri']
        tracks_list.append(track_id)
    except: 
        print(f"track:{song['name']} artist:{song['artist']}")
        continue

user_id = sp.current_user()['id']
playlist_id = sp.user_playlist_create(user_id, f'{date} Top 100 Bill Board', public=True, collaborative=False, description='')['id']

sp.playlist_add_items(playlist_id=playlist_id, items=tracks_list)
