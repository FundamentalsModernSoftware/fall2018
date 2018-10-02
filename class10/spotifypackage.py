import spotipy
from spotifySecrets import *
from spotipy.oauth2 import SpotifyClientCredentials
import sys

# Authenticate with Spotify
ccm = SpotifyClientCredentials(client_id = CLIENT_ID,
                               client_secret = CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=ccm)

# Find top artist matching the user's search
artistName = ' '.join(sys.argv[1:])
results = sp.search(q=artistName, type='artist')
artist = results['artists']['items'][0]

# Find top 10 tracks by that artist
results = sp.artist_top_tracks(artist['uri'])
for track in results['tracks']:
    print(track['name'])
