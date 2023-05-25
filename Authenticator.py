from Credentials import CLIENT_ID, CLIENT_SECRET
from spotipy.oauth2 import SpotifyClientCredentials
from Crawler import Crawler
import urllib.request
import spotipy

class Authenticator:

    def __init__(self, profileLink):
        self.auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        self.sp = spotipy.Spotify(auth_manager= self.auth_manager)

        self.playlists = self.sp.user_playlists(profileLink)
        self.artists_list = []

    def scanProfile(self):
        while self.playlists:
            for i, playlist in enumerate(self.playlists['items']):
                tracks = self.sp.playlist_items(playlist_id=playlist['id'], fields=["items"], offset=0, limit=100)
                for tr in tracks["items"]:
                    # print(tr["track"]["name"], tr["track"]["artists"][0]["id"], tr["track"]["artists"][0]["name"],  "\n")
                    id = tr["track"]["artists"][0]["id"]
                    if id not in self.artists_list:
                        self.artists_list.append(id)

            if self.playlists['next']:
                self.playlists = self.sp.next(self.playlists)
            else:
                self.playlists = None

        for link in self.artists_list:
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