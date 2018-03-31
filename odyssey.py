import logging as LOG
from common.user import User

def getUniqueTracks(username):
    trackDict = {}
    user = User(username)
    for playlist in user.playlists().values():
        trackDict = {** trackDict, **{track.uri: track for track in playlist.tracks()}}
    return trackDict
