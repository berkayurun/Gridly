import json
import os
import pathlib
import shutil
import requests
import image
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
    parser.add_argument("--all", "-A", help="Create album, artist and song collages",
                        action="store_true")
    parser.add_argument("--album", "-a", help="Create album collage",
                        action="store_true")
    parser.add_argument("--artist", "-b", help="Create artist collage",
                        action="store_true")
    parser.add_argument("--song", "-s", help="Create song collage",
                        action="store_true")
    parser.add_argument("--skip", help="Skip items without covers",
                        action="store_true")
    parser.add_argument("--exclude", '-e', help="Exclude the artists",
                        nargs='+', type=str)
    parser.add_argument("--config", '-c', help="Configure the config file",
                        action="store_true")
    args = parser.parse_args()
    return args


def config(reconfig=False):
    if os.path.exists('./config/config.txt') and not reconfig:
        return
    elif os.path.exists('./config/config.txt') and reconfig:
        os.remove('./config/config.txt')

    if not os.path.exists('./config'):
        os.mkdir('./config')

    print('First time config is running...')
    api_key = input("Please input your Last.fm API key: ")
    client_id = input("Please input your Spotify client id: ")
    client_secret = input("Please input your Spotify client secret: ")
    with open('./config/config.txt', 'w') as f:
        f.write(f"{api_key}\n")
        f.write(f"{client_id}\n")
        f.write(f"{client_secret}\n")

    print('Config completed...')
    if reconfig:
        exit(0)

    return


def main():
    utils.register_signal_handler()
    args = parse_arguments()
    config(args.config)
    print('Collages are being created...')
    size = args.x * args.y

    if (args.album or args.all) or (not args.artist and not args.song):
        albums = Album.get_albums_of_year(
            args.username, size, args.skip, args.exclude)
        create_save_collage(albums, args.x, args.y)
    if args.artist or args.all:
        artists = Artist.get_artists_of_year(
            args.username, size, args.skip, args.exclude)
        create_save_collage(artists, args.x, args.y)
    if args.song or args.all:
        songs = Song.get_songs_of_year(
            args.username, size, args.skip, args.exclude)
        create_save_collage(songs, args.x, args.y)


main()
