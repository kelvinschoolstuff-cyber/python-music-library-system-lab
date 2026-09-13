class Song:
    """Represent a song and maintain aggregate library statistics."""

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count = {}
    # Keep the original singular name available for existing consumers.
    artist_count = artists_count

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_genres(self.genre)
        self.add_to_artists(self.artist)
        self.add_to_genre_count(self.genre)
        self.add_to_artists_count(self.artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artists_count(cls, artist):
        count = cls.artists_count.get(artist, 0) + 1
        cls.artists_count[artist] = count
        # Synchronize the legacy singular attribute used by older clients.
        cls.artist_count[artist] = count
