import random
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


SCOPE = "user-read-playback-state,user-modify-playback-state,user-library-read"


class Spotify:
    def __init__(self):
        self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                                               client_secret=CLIENT_SECRET,
                                                                               redirect_uri="http://localhost:8888/callback/",
                                                                               scope=SCOPE))

    @property
    def user(self):
        return self.spotify.current_user()

    def get_playlists(self):
        """Gets playlists created by user"""
        return self.spotify.current_user_playlists()

    def get_liked_songs(self):
        #TODO: can't get playlist of liked songs
        return self.spotify.current_user_saved_shows()

    def get_playlists_ids(self):
        """Gets playlists name created by user"""
        playlist_data = self.get_playlists()['items']
        playlist_ids = [playlist['id'] for playlist in playlist_data]
        return playlist_ids

    def get_random_playlist_id(self):
        """Choosing randomly playlist name"""
        return random.choice(self.get_playlists_ids())

    #TODO: add non-mandatory param as liked songs
    def get_random_song_uri(self):
        playlist_id = self.get_random_playlist_id()
        songs = self.spotify.user_playlist_tracks(playlist_id=playlist_id)
        uris = [track['track']['uri'] for track in songs['items']]
        return [random.choice(uris)]

    def playing_devices(self):
        return self.spotify.devices()

    def play_song(self):
        uri = self.get_random_song_uri()
        device_id = ''
        for device in self.playing_devices()['devices']:
            if device["name"] == "Anna Sharkova\'s MBP":
                device_id = device["id"]
        self.spotify.start_playback(device_id=device_id, uris=uri)

        # Change volume
        for volume in range(10, 100, 10):
            self.spotify.volume(volume_percent=volume, device_id=device_id)
            time.sleep(1)


if __name__ == '__main__':
    spoty = Spotify()
    uri = spoty.get_random_song_uri()
    spoty.play_song()
