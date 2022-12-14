import json
import pathlib
import shutil
import requests
import image
import config
import argparse
import utils
from album import Album
from artist import Artist
from song import Song


def get_json_string(response):
    """Dump response to a string"""
    return json.dumps(response.json(), sort_keys=True, indent=4)


def create_save_collage(lastfmObjectArray, x, y):
    pathlib.Path('./cache').mkdir(parents=True, exist_ok=True)
    for i in lastfmObjectArray:
        i.download_picture()

    image.create_collage(lastfmObjectArray, x, y)

    shutil.rmtree('./cache')


def parse_arguments():
    parser = argparse.ArgumentParser(description='Collage creator for LastFM')
    parser.add_argument("x", help="Horizontal size of the collage",
                        type=int)
    parser.add_argument("y", help="Vertical size of the collage",
                        type=int)
    parser.add_argument("username", help="Username")
    parser.add_argument("--album", "-a", help="Create album collage",
                        action="store_true")
    parser.add_argument("--artist", "-b", help="Create artist collage",
                        action="store_true")
    parser.add_argument("--song", "-s", help="Create song collage",
                        action="store_true")
    parser.add_argument("--skip", help="Skip items without covers",
                        action="store_true")
    args = parser.parse_args()
    return args


def main():
    utils.register_signal_handler()
    args = parse_arguments()
    size = args.x * args.y

    if args.album or (not args.artist and not args.song):
        albums = Album.get_albums_of_year(args.username, size, args.skip)
        create_save_collage(albums, args.x, args.y)
    if args.artist:
        artists = Artist.get_artists_of_year(args.username, size)
        create_save_collage(artists, args.x, args.y)
    if args.song:
        songs = Song.get_songs_of_year(args.username, size)
        create_save_collage(songs, args.x, args.y)


main()
