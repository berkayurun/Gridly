from lastfm import LastfmObject
from math import sqrt


class Artist(LastfmObject):
    def get_artists_of_year(username, size):
        API_KEY = utils.get_api_key()
        # Gets more than needed, so that if some albums
        # miss cover, they can be replaced
        payload = {
            "api_key": API_KEY,
            "user": username,
            "method": "user.getTopArtists",
            "format": "json",
            "limit": size + round(sqrt(size)),
            "period": "12month",
        }

        response = LastfmObject.make_request(payload)

        artist_list = []
        index = 0
        for artist_instance in response.json()["topartists"]["artist"]:
            if index >= size:
                break

            artist_name = artist_instance["name"]
            artist_listen_count = artist_instance["playcount"]
            artist_picture = artist_instance["image"][3]["#text"]

            if not album_picture and skip_no_covers:
                continue

            artist_mbid = artist_instance["mbid"]
            artist_list.append(
                Artist(
                    name=artist_name,
                    mbid=artist_mbid,
                    listen_count=artist_listen_count,
                    picture_link=artist_picture,
                )
            )

        return artist_list
