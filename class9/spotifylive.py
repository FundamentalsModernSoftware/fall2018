import requests
from base64 import b64encode
from spotifysecrets import *
import sys

AUTHENTICATION_URL = 'https://accounts.spotify.com/api/token'
SEARCH_URL = 'https://api.spotify.com/v1/search'
TOP_TRACKS_URL = 'https://api.spotify.com/v1/artists/'

# Authenticate with Spotify
headers = {'Authorization':
           b'Basic ' + b64encode(CLIENT_ID + b':' + CLIENT_SECRET)}
body = {'grant_type': 'client_credentials'}
r = requests.post(AUTHENTICATION_URL, headers=headers, data=body)