import os
from lastfm import LastfmObject
import requests


class Album(LastfmObject):
    def __init__(self, artist_name, listen_count, picture_link, album_name):
        super().__init__(artist_name, listen_count, picture_link)
        self.album_name = album_name

    def print(self):
        print(f"Album Name: {self.album_name}")
        super().print()

    def download_picture(self):
        r = requests.get(self.picture_link, allow_redirects=True)
        open(f"./cache/{self.album_name}.jpg", "wb").write(r.content)

    def delete_picture(self):
        os.remove(f"./cache/{self.album_name}.jpg")
