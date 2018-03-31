from common.track import Track

def getTracksFromDump(dump, client):
    tracks = []
    results = client.user_playlist(dump['owner']['id'], dump['id'], fields='tracks,next')
    if results:
        page = results['tracks']
        tempTracks = [Track(trackDump) for trackDump in page['items']]
        tracks = [*tracks, *tempTracks]
        while page['next']:
            page = client.next(page)
            tempTracks = [Track(trackDump) for trackDump in page['items']]
            tracks = [*tracks, *tempTracks]
    return tracks

class Playlist:
    def __init__(self, dump, client):
        self._spotify_dump = dump
        self.client = client
        self.uri = dump['uri']
        self.title = dump['name']
        self.owner = dump['owner']['id']
        self._tracks = []

    def tracks(self):
        if self._tracks == []:
            self._tracks = getTracksFromDump(self._spotify_dump, self.client)
        return self._tracks

    def toJson(self):
        return {
            'uri': self.uri,
            'title': self.title,
            'owner': self.owner,
            'tracks': [track.toJson() for track in self.tracks()]
        }
