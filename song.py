from lastfm import LastfmObject
import config

API_KEY = config.API_KEY
USER = config.USER


class Song(LastfmObject):
    def __init__(self, name, listen_count, picture_link, artist_name):
        super().__init__(name, listen_count, picture_link)
        self.artist_name = artist_name

    def print(self):
        super().print()
        print(f"Artist Name: {self.artist_name}")

    def get_songs_of_year():
        payload = {
            "api_key": API_KEY,
            "user": USER,
            "method": "user.getTopTracks",
            "format": "json",
            "limit": 25,
            "period": "12month",
        }

        response = LastfmObject.make_request(payload)

        song_list = []

        for song_instance in response.json()["toptracks"]["track"]:
            song_name = song_instance["name"]
            song_listen_count = song_instance["playcount"]
            songs_artist = song_instance["artist"]["name"]
            song_picture = song_instance["image"][3]["#text"]
            song_list.append(
                Song(
                    name=song_name,
                    listen_count=song_listen_count,
                    picture_link=song_picture,
                    artist_name=songs_artist,
                )
            )

        return song_list
