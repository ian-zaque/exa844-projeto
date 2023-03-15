from Credentials import CLIENT_ID, CLIENT_SECRET, USER
import urllib.request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from Crawler import Crawler

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists(USER)
artists_list = []

while playlists:
    for i, playlist in enumerate(playlists['items']):
        tracks = sp.playlist_items(playlist_id=playlist['id'], fields=["items"], offset=0, limit=100)
        for tr in tracks["items"]:
            # print(tr["track"]["name"], tr["track"]["artists"][0]["id"], tr["track"]["artists"][0]["name"],  "\n")
            id = tr["track"]["artists"][0]["id"]
            if id not in artists_list:
                artists_list.append(id)

    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

for link in artists_list:
    link = "https://open.spotify.com/artist/"  + link
    link = link.strip()
    page = urllib.request.urlopen(link)
    html = str(page.read().decode('utf-8'))

    craw = Crawler(html, link)
    craw.setSections()
    craw.extractMusicInfo("albums")
    craw.extractMusicInfo("singles")
    craw.extractMusicInfo("similarArtists")
    craw.createJson()