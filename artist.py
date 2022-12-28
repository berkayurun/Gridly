from lastfm import LastfmObject
import utils


class Artist(LastfmObject):
    def get_artists_of_year(username, size, skip_no_covers, exclude_list
                            ):
        API_KEY = utils.get_api_key()
        # Gets more than needed, so that if some albums
        # miss cover, they can be replaced
        payload = {
            "api_key": API_KEY,
            "user": username,
            "method": "user.getTopArtists",
            "format": "json",
            "limit": 2 * size,
            "period": "12month",
        }

        response = LastfmObject.make_request(payload)

        artist_list = []
        index = 0
        for artist_instance in response.json()["topartists"]["artist"]:
            if index >= size:
                break

            artist_name = artist_instance["name"]

            if exclude_list:
                if artist_name in exclude_list:
                    continue

            artist_listen_count = artist_instance["playcount"]
            artist_picture = LastfmObject.get_cover_from_spotify(
                artist_name, 'artist')

            if not artist_picture and skip_no_covers:
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

            index = index + 1

        return artist_list
