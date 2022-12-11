from lastfm import LastfmObject
import config

API_KEY = config.API_KEY
USER = config.USER

class Artist(LastfmObject):
    def get_artists_of_year():
        payload = {
            "api_key": API_KEY,
            "user": USER,
            "method": "user.getTopArtists",
            "format": "json",
            "limit": 25,
            "period": "12month",
        }

        response = LastfmObject.make_request(payload)

        artist_list = []

        for artist_instance in response.json()["topartists"]["artist"]:
            artist_name = artist_instance["name"]
            artist_listen_count = artist_instance["playcount"]
            artist_picture = artist_instance["image"][3]["#text"]
            artist_list.append(
                Artist(
                    name=artist_name,
                    listen_count=artist_listen_count,
                    picture_link=artist_picture,
                )
            )

        return artist_list