from lastfm import LastfmObject
import config

API_KEY = config.API_KEY
USER = config.USER

class Album(LastfmObject):
    def __init__(self, name, listen_count, picture_link, artist_name):
        super().__init__(name, listen_count, picture_link)
        self.artist_name = artist_name

    def print(self):
        super().print()
        print(f"Artist Name: {self.artist_name}")

    def get_albums_of_year():
        payload = {
            "api_key": API_KEY,
            "user": USER,
            "method": "user.getTopAlbums",
            "format": "json",
            "limit": 25,
            "period": "12month",
        }

        response = LastfmObject.make_request(payload)

        album_list = []

        for album_instance in response.json()["topalbums"]["album"]:
            album_name = album_instance["name"]
            album_listen_count = album_instance["playcount"]
            albums_artist = album_instance["artist"]["name"]
            album_picture = album_instance["image"][3]["#text"]
            album_list.append(
                Album(
                    name=album_name,
                    listen_count=album_listen_count,
                    picture_link=album_picture,
                    artist_name=albums_artist,
                )
            )

        return album_list