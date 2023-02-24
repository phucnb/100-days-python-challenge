# Creates a playlist for a user

import argparse
import logging
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SP_ID = os.environ.get('SPOTIFY_ID')
SP_KEY = os.environ.get('SPOTIFY_KEY')
logger = logging.getLogger('examples.create_playlist')
logging.basicConfig(level='DEBUG')


def get_args():
    parser = argparse.ArgumentParser(description='Creates a playlist for user')
    parser.add_argument('-p', '--playlist', required=True,
                        help='Name of Playlist')
    parser.add_argument('-d', '--description', required=False, default='',
                        help='Description of Playlist')
    return parser.parse_args()


def main():
    args = get_args()
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SP_ID,
                                               client_secret=SP_KEY,
                                               redirect_uri="http://example.com",
                                               scope="user-library-read"))
    user_id = sp.me()['id']
    sp.user_playlist_create(user_id, args.playlist)


if __name__ == '__main__':
    main()