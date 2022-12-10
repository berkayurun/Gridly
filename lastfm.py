class LastfmObject:
    def __init__(self, artist_name, listen_count, picture_link):
        self.artist_name = artist_name
        self.listen_count = listen_count
        self.picture_link = picture_link

    def print(self):
        print(
            f"Artist Name: {self.artist_name}\n"
            + f"Listen Count: {self.listen_count}\n"
            + f"Picture Link: {self.picture_link}\n"
        )
