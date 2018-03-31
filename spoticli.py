import sys
import time
import argparse
import pprint
import odyssey
import util
import logging as LOG

LOG.basicConfig(level=LOG.INFO)
pp = pprint.PrettyPrinter(indent=4)

def _interactive(parser):
    LOG.info('Interactive Mode')
    LOG.info('To be implemented!')

def _alexandria(parser):
    LOG.info('Alexandria: Playlist collection import/export')
    LOG.info('To be implemented!')

def _odyssey(parser):
    LOG.info('Odyssey: Playlist collection analysis')
    LOG.info(f"Looking for all unique tracks in {parser.parse_args().username)}'s playlists...")
    LOG.info(f"You have used {len(odyssey.getUniqueTracks(parser.parse_args().username))} unique tracks in your playlists. Look at you!")

def spotiCLI():
    description = 'Gets information about tracks in a user\'s playlists'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('username', type=str, help='Your spotify username')
    subparsers = parser.add_subparsers(title='subcommand', dest='subcommand')

    interactiveParser = subparsers.add_parser('interactive')

    odysseyParser = subparsers.add_parser('odyssey', help='Analyzes playlists for interesting data')
    odysseyParser.add_argument('action', choices=['uniqueTracks'], help='Calculates the total number of unique songs youve used in all your playlists')

    alexandriaParser = subparsers.add_parser('alexandria', help='Manages imports/exports of a playlist collection')
    alexandriaParser.add_argument('action', choices=['import', 'export'], help='indicate which action you want to take')
    alexandriaParser.add_argument('file')

    parser.add_argument('-v', '--verbose', action='store_true', help='Prints out info about individual playlists and program runtime')
    if(parser.parse_args().verbose):
        LOG.getLogger().setLevel(level=LOG.DEBUG)

    options = {
        'interactive': _interactive,
        'alexandria': _alexandria,
        'odyssey': _odyssey
    }
    options[parser.parse_args().subcommand](parser)

if __name__ == '__main__':
    start_time = time.clock()
    spotiCLI()
    LOG.debug(f"Program executed in {round(time.clock() - start_time, 2)} seconds.")
