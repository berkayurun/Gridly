import json
import requests
import image
import config
from album import Album
from artist import Artist
from song import Song

X_SIZE = 5
Y_SIZE = 10


def get_json_string(response):
    """Dump response to a string"""
    return json.dumps(response.json(), sort_keys=True, indent=4)


def create_save_collage(lastfmObjectArray):
    for i in lastfmObjectArray:
        i.download_picture()

    image.create_collage(lastfmObjectArray, X_SIZE, Y_SIZE)

    for i in lastfmObjectArray:
        i.delete_picture()


def main():
    albums = Album.get_albums_of_year(X_SIZE, Y_SIZE)
    artists = Artist.get_artists_of_year(X_SIZE, Y_SIZE)
    songs = Song.get_songs_of_year(X_SIZE, Y_SIZE)

    create_save_collage(albums)
    create_save_collage(artists)
    create_save_collage(songs)


main()
