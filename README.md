 # spotiCLI

A simple command line tool for gathering and analyzing Spotify account information. In the future, this may include tools for manipulating playlists.

 ## Setup

 Clone this repo locally and add your `config.json` file to the root directory. spotiCLI has the following dependencies:
 - [Python 3.6](https://www.python.org/downloads/release/python-360/)
 - [spotipy](https://github.com/plamere/spotipy). Once python is installed use `pip install spotipy` to download and install the package


 ### Getting `config.json`

 1. Log into the [Spotify Developer website](https://beta.developer.spotify.com/dashboard/) and click 'Create a Client ID'. Follow the instructions in the wizard.
 2. Save the client ID and secret in a file named `config` with the following formatting:

 ```
 {
   "client_id": <YOUR_CLIENT_ID>,
   "client_secret": <YOUR_CLIENT_SECRET>
 }
 ```


 ## Tools

 ### Odyssey

 Odyssey handles all of your playlist collection analysis. Currently the only functionality built in is for getting all unique tracks used in your playlists.

 Usage: `python spoticli.py (-v --verbose) <SPOTIFY_USERNAME> odyssey uniqueTracks`

 ### Alexandria

 Alexandria handles importing and exporting your playlists to and from Spotify. This is primarily intended for backing up your playlist information should something happen to your account.

 Alexandria is still under development.
