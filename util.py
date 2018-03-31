import json
import spotipy
import spotipy.util as util
import logging as LOG

def getAPICredentials(filepath = './config.json'):
    with open(filepath) as config:
        return json.loads(config.read())

def getSpotifyClient(username, scope='playlist-read-private playlist-read-collaborative'):
    creds = getAPICredentials()
    app_redirect = 'http://localhost/'
    token = util.prompt_for_user_token(username, scope, client_id=creds['client_id'], client_secret=creds['client_secret'], redirect_uri=app_redirect)
    if token:
        LOG.info(f"Authenticated {username} successfully!")
        return spotipy.Spotify(auth=token)
    else:
        LOG.error(f"Can't get token for {username}")
        return null
