import logging as LOG

class Track:
    def __init__(self, dump):
        self._spotify_dump = dump
        self.uri = dump['track']['uri']
        self.title = dump['track']['name']
        self.artists = [artist['name'] for artist in dump['track']['artists']]
        self.album = dump['track']['album']['name']

    def toJson(self):
        return {
            'uri': self.uri,
            'title': self.title,
            'artists': self.artists,
            'album': self.album
        }
