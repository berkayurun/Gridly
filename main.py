import json
import requests
import image
import config
from album import Album

API_KEY = config.API_KEY
USER = config.USER


def get_json_string(response):
    """Dump response to a string"""
    return json.dumps(response.json(), sort_keys=True, indent=4)


def make_request(parameters):
    headers = {"user-agent": USER}

    return requests.get(
        "https://ws.audioscrobbler.com/2.0/",
        headers=headers,
        params=parameters
        )


def get_albums_of_year():
    payload = {
        "api_key": API_KEY,
        "user": USER,
        "method": "user.getTopAlbums",
        "format": "json",
        "limit": 25,
        "period": "12month",
    }

    response = make_request(payload)

    album_list = []

    for album_instance in response.json()["topalbums"]["album"]:
        album_name = album_instance["name"]
        album_listen_count = album_instance["playcount"]
        albums_artist = album_instance["artist"]["name"]
        album_picture = album_instance["image"][3]["#text"]
        album_list.append(
            Album(
                artist_name=albums_artist,
                listen_count=album_listen_count,
                picture_link=album_picture,
                album_name=album_name,
            )
        )

    return album_list


def main():
    albums = get_albums_of_year()

    for i in albums:
        i.download_picture()

    image.create_collage(albums)

    for i in albums:
        i.delete_picture()


main()
