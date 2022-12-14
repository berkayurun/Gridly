from lastfm import LastfmObject
import config
from math import sqrt

API_KEY = config.API_KEY
USER = config.USER


class Song(LastfmObject):
    def __init__(self, name, mbid, listen_count, picture_link, artist_name):
        super().__init__(name, mbid, listen_count, picture_link)
        self.artist_name = artist_name

    def print(self):
        super().print()
        print(f"Artist Name: {self.artist_name}")

    def get_songs_of_year(username, size):
        # Gets more than needed, so that if some albums
        # miss cover, they can be replaced
        payload = {
            "api_key": API_KEY,
            "user": username,
            "method": "user.getTopTracks",
            "format": "json",
            "limit": size + round(sqrt(size)),
            "period": "12month",
        }

        response = LastfmObject.make_request(payload)

        song_list = []
        index = 0
        for song_instance in response.json()["toptracks"]["track"]:
            if index >= size:
                break
            song_name = song_instance["name"]
            song_listen_count = song_instance["playcount"]
            songs_artist = song_instance["artist"]["name"]
            song_picture = song_instance["image"][3]["#text"]

            if not album_picture and skip_no_covers:
                continue

            song_mbid = song_instance["mbid"]
            song_list.append(
                Song(
                    name=song_name,
                    mbid=song_mbid,
                    listen_count=song_listen_count,
                    picture_link=song_picture,
                    artist_name=songs_artist,
                )
            )

        return song_list
