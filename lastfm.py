import requests
import os
import utils
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class LastfmObject:
    def __init__(self, name, mbid, listen_count, picture_link):
        self.name = name
        self.mbid = mbid
        self.listen_count = listen_count
        self.picture_link = picture_link

    def print(self):
        print(
            f"Name: {self.name}\n"
            + f"Listen Count: {self.listen_count}\n"
            + f"Picture Link: {self.picture_link}\n"
        )

    def get_cover_from_spotify(name: str, obj_type: str, artist_name: str = None):
        ''' Returns the cover link from Spotify'''
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=utils.get_client_id(),
                                                                   client_secret=utils.get_client_secret()))

        if artist_name:
            results = sp.search(q='artist: ' + artist_name + ', ' + obj_type + ': ' + name,
                                type=obj_type, market='DE', limit=1)
        else:
            results = sp.search(q=obj_type + ': ' + name,
                                type=obj_type, market='DE', limit=1)
        items = results[obj_type + 's']['items']
        if len(items) > 0:
            obj = items[0]
            try:
                if obj_type == 'track':
                    return obj['album']['images'][0]['url']
                elif obj_type == 'artist':
                    return obj['images'][0]['url']
            except:
                return ''

    def download_picture(self):
        if self.picture_link:
            r = requests.get(self.picture_link, allow_redirects=True)
            open(f"./cache/{utils.get_image_name(self)}",
                 "wb").write(r.content)

    def delete_picture(self):
        try:
            os.remove(f"./cache/{utils.get_image_name(self)}")
        except:
            None

    def make_request(parameters):

        return requests.get(
            "https://ws.audioscrobbler.com/2.0/",
            params=parameters
        )
