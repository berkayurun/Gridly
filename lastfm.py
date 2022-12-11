import requests
import os
import config

API_KEY = config.API_KEY
USER = config.USER


class LastfmObject:
    def __init__(self, name, listen_count, picture_link):
        self.name = name
        self.listen_count = listen_count
        self.picture_link = picture_link

    def print(self):
        print(
            f"Name: {self.name}\n"
            + f"Listen Count: {self.listen_count}\n"
            + f"Picture Link: {self.picture_link}\n"
        )

    def download_picture(self):
        r = requests.get(self.picture_link, allow_redirects=True)
        print(f"URL: {self.picture_link}")
        open(f"./cache/{self.name}.jpg", "wb").write(r.content)

    def delete_picture(self):
        os.remove(f"./cache/{self.name}.jpg")

    def make_request(parameters):
        headers = {"user-agent": USER}

        return requests.get(
            "https://ws.audioscrobbler.com/2.0/",
            headers=headers,
            params=parameters
        )
