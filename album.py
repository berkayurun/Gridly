from lastfm import LastfmObject
import utils


class Album(LastfmObject):
    def __init__(self, name, mbid, listen_count, picture_link, artist_name):
        super().__init__(name, mbid, listen_count, picture_link)
        self.artist_name = artist_name

    def print(self):
        super().print()
        print(f"Artist Name: {self.artist_name}")

    def get_albums_of_year(username: str, size: int, skip_no_covers: bool, exclude_list):
        API_KEY = utils.get_api_key()

        # Gets more than needed, so that if some albums
        # miss cover, they can be replaced
        payload = {
            "api_key": API_KEY,
            "user": username,
            "method": "user.getTopAlbums",
            "format": "json",
            "limit": 2 * size,
            "period": "12month",
        }

        response = LastfmObject.make_request(payload)

        album_list = []
        index = 0
        for album_instance in response.json()["topalbums"]["album"]:
            if index >= size:
                break

            album_name = album_instance["name"]
            album_listen_count = album_instance["playcount"]
            albums_artist = album_instance["artist"]["name"]

            if albums_artist in exclude_list:
                continue

            album_picture = album_instance["image"][3]["#text"]

            if not album_picture and skip_no_covers:
                continue

            album_mbid = album_instance["mbid"]
            album_list.append(
                Album(
                    name=album_name,
                    mbid=album_mbid,
                    listen_count=album_listen_count,
                    picture_link=album_picture,
                    artist_name=albums_artist,
                )
            )

            index = index + 1

        return album_list
