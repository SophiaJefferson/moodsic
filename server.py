import sys
from flask import Flask, render_template, request, redirect, Response, send_from_directory
import random, json
import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

moods_to_music = {'anger': ['Get Turnt', 'Rock Hard'],
                'contempt': ['Down in the Dumps', 'Most Necessary'],
                'disgust': ['Move On & Don\'t Look Back'],
                'fear': ['Tender', 'Techno Bunker'],
                'happiness': ['Have a Great Day!', 'Happy Hits!'],
                'neutral': ['Your Favorite Coffeehouse', 'chill.out.brain'],
                'sadness': ['Melancholia', 'Life Sucks'],
                'surprise': ['Songs to Sing in the Shower', 'Energizing Hits']}

is_authenticated = False

@app.route('/')
def index():
	# serve index template
	return render_template('index.html', name='Joe')

# given primary mood returns playlist
@app.route('/getPlaylist', methods = ['GET', 'POST'])
def getPlaylist():
	print request.form
	primaryEmotion = list(request.form.to_dict().keys())[0]
	if (not is_authenticated):
		authenticate()
	
	playMood(primaryEmotion)

	return render_template('index.html', name='Jose')

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
    # return render_template('index.html', appName=name)

def authenticate():
    # username = "travrb16"
    # token = util.prompt_for_user_token(username, 
        # client_id='1ba453bd75d044359b41ff526bc9ba48',
        # client_secret='8fb7cca3f3424cc3ac17911b810397cd',
        # redirect_uri="http://localhost:5000/callback")
    global sp
    client_credentials_manager = SpotifyClientCredentials(client_id='1ba453bd75d044359b41ff526bc9ba48', client_secret='8fb7cca3f3424cc3ac17911b810397cd')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)    

def playMood(primaryMood):
    playlist = random.choice(moods_to_music[primaryMood])
    search = sp.search(playlist, type='playlist')['playlists']['items']
    for term in search:
        if term['name'] == playlist:
            moodsic_uri = term['uri']
            break

    sp.start_playback(device_id="travrb16", context_uri=moodsic_uri, uris=None, offset=None)

if __name__ == '__main__':
	app.run()


