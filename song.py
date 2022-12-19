from lastfm import LastfmObject
import utils


class Song(LastfmObject):
    def __init__(self, name, mbid, listen_count, picture_link, artist_name):
        super().__init__(name, mbid, listen_count, picture_link)
        self.artist_name = artist_name

    def print(self):
        super().print()
        print(f"Artist Name: {self.artist_name}")

    def get_songs_of_year(username, size, skip_no_covers, exclude_list
                          ):
        API_KEY = utils.get_api_key()
        # Gets more than needed, so that if some albums
        # miss cover, they can be replaced
        payload = {
            "api_key": API_KEY,
            "user": username,
            "method": "user.getTopTracks",
            "format": "json",
            "limit": 2 * size,
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

            if songs_artist in exclude_list:
                continue

            song_picture = LastfmObject.get_cover_from_spotify(song_name,
                                                               'track', songs_artist)
            if not song_picture and skip_no_covers:
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

            index = index + 1
        return song_list
