import logging as LOG
import util
from common.playlist import Playlist

def getUserPlaylists(username, client):
    playlists = {}
    results = client.user_playlists(username)
    if results:
        temp = {playlist['id']: Playlist(playlist, client) for playlist in results['items']}
        playlists = {**playlists, **temp}
        while results['next']:
            results = client.next(results)
            temp = {playlist['id']: Playlist(playlist, client) for playlist in results['items']}
            playlists = {**playlists, **temp}
    return playlists

class User:
    def __init__(self, username):
        self.username = username
        self.client = util.getSpotifyClient(username)
        self._playlists = {}

    def playlists(self):
        if self._playlists == {}:
            self._playlists = getUserPlaylists(self.username, self.client)
            # __playlists = self.client.user_playlists(self.username)
        return self._playlists

    def playlist(self, id):
        try:
            _playlist = self.playlists()[id]
        except KeyError:
            LOG.error('Playlist not found!')
            return null
        return _playlist

    def toJson(self):
        return {
            'id': self.username,
            'playlists': [playlist.toJson() for playlist in self.playlists().values()]
        }
