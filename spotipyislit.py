import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='1ba453bd75d044359b41ff526bc9ba48', client_secret='8fb7cca3f3424cc3ac17911b810397cd')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.featured_playlists(limit=50)

for playlist in playlists['playlists']['items']:
    print playlist['name']
    print playlist['external_urls']['spotify']