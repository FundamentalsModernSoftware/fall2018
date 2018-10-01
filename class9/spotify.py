import requests, sys
from spotifysecrets import *
from base64 import b64encode

AUTHENTICATION_URL = 'https://accounts.spotify.com/api/token'

# Authenticate with Spotify
headers = {'Authorization':
           b'Basic ' + b64encode(CLIENT_ID + b':' + CLIENT_SECRET)}
body = {'grant_type': 'client_credentials'}
r = requests.post(AUTHENTICATION_URL, headers=headers, data=body)

token = r.json()['access_token']
tokenHeaders = {'Authorization' : 'Bearer ' + token}

SEARCH_URL = 'https://api.spotify.com/v1/search'
TOP_TRACKS_URL = 'https://api.spotify.com/v1/artists/'

# Find top artist matching the user's search
artistName = ' '.join(sys.argv[1:])
query = {'q': artistName, 'type': 'artist'}
r = requests.get(SEARCH_URL, headers=tokenHeaders, params=query)
artist = r.json()['artists']['items'][0]

# Find top 10 tracks by that artist
url = TOP_TRACKS_URL + artist['id'] + '/top-tracks'
query = {'country': 'US'}
r = requests.get(url, headers=tokenHeaders, params=query)
for track in r.json()['tracks']:
    print(track['name'])
