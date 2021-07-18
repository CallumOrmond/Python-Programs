import spotipy
import pprint
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

#TEST CHANGE

#WORKING 

scope = 'user-top-read user-read-recently-played user-read-playback-state playlist-modify-public playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


CurrentPlayingName = sp.current_user_playing_track()['item']['name']
CurrentPlayingID = sp.current_user_playing_track()['item']['id']


#Check and make new playlist, no dublicates
results = sp.current_user_playlists(limit=50)
PlayLists = []
for item in (results['items']):
    PlayLists.append(item['name'])

if "Auto PlayList" not in PlayLists:
	user_id = sp.me()['uri']
	sp.user_playlist_create(user_id,"Auto PlayList")

#get playlist id
for item in (results['items']):
	if item['name'] == "Auto PlayList":
		PlayListID = item['uri']

print(CurrentPlayingName, CurrentPlayingID , "\n")

sp.playlist_add_items(PlayListID, [CurrentPlayingID])

