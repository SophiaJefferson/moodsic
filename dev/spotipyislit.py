import spotipy
from spotipy import util
import random
from spotipy.oauth2 import SpotifyClientCredentials

username = "beastmo_11"
token = util.prompt_for_user_token(username, client_id='1ba453bd75d044359b41ff526bc9ba48', client_secret='8fb7cca3f3424cc3ac17911b810397cd')

if not token:
	print "Can\'t get token for", username


client_credentials_manager = SpotifyClientCredentials(client_id='1ba453bd75d044359b41ff526bc9ba48', client_secret='8fb7cca3f3424cc3ac17911b810397cd')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, auth=token)

print sp.me()

# playlists = sp.featured_playlists(limit=50)

moods_to_music = {'anger': ['Get Turnt', 'Rock Hard'],
				'contempt': ['Down in the Dumps', 'Most Necessary'],
				'disgust': ['Move On & Don\'t Look Back'],
            	'fear': ['Tender', 'Techno Bunker'],
            	'happiness': ['Have a Great Day!', 'Happy Hits!'],
            	'neutral': ['Your Favorite Coffeehouse', 'chill.out.brain'],
            	'sadness': ['Melancholia', 'Life Sucks'],
            	'surprise': ['Songs to Sing in the Shower', 'Energizing Hits']}

# moodsic = random.choice(moods_to_music[mood])

playlists = sp.user_playlists('spotify')
moodsic = 'Get Turnt'
search = sp.search(moodsic, type='playlist')['playlists']['items']
for term in search:
    if term['name'] == moodsic:
        moodsic_uri = term['uri']
        break



# start_playback(device_id=None, context_uri=None, uris=None, offset=None)
sp.start_playback(device_id="travrb10", context_uri=moodsic_uri, uris=None, offset=None)


# print playlists['items']


# for playlst in playlists['items']:
#     print playlst['name']
    # if playlst['name'] == 'Get Turnt':
    #     uri = playlst['uri']
    #
    #     print uri
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print(playlists['offset'], playlist['uri'],  playlist['name'])
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None