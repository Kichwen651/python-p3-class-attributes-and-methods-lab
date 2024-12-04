class Song:
    count = 0  # Class attribute to keep track of how many songs are created
    genres = []  # List to store unique genres
    artists = []  # List to store unique artists
    genre_count = {}  # Dictionary to store count of each genre
    artist_count = {}  # Dictionary to store count of each artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call the methods to update class attributes
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1  # Increment the song count

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)  # Add genre to the list if it's not already present

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)  # Add artist to the list if it's not already present

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1  # Increment the count if genre already exists
        else:
            cls.genre_count[genre] = 1  # Otherwise, initialize the count for this genre

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1  # Increment the count if artist already exists
        else:
            cls.artist_count[artist] = 1  # Otherwise, initialize the count for this artist


# Example Usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
print(ninety_nine_problems.name)  # "99 Problems"
print(ninety_nine_problems.artist)  # "Jay-Z"
print(ninety_nine_problems.genre)  # "Rap"

print(Song.count)  # 1
print(Song.genres)  # ['Rap']
print(Song.artists)  # ['Jay-Z']
print(Song.genre_count)  # {'Rap': 1}
print(Song.artist_count)  # {'Jay-Z': 1}

# Adding more songs
song2 = Song("Hard Knock Life", "Jay-Z", "Rap")
song3 = Song("Bohemian Rhapsody", "Queen", "Rock")
song4 = Song("I Walk the Line", "Johnny Cash", "Country")

print(Song.count)  # 4
print(Song.genres)  # ['Rap', 'Rock', 'Country']
print(Song.artists)  # ['Jay-Z', 'Queen', 'Johnny Cash']
print(Song.genre_count)  # {'Rap': 2, 'Rock': 1, 'Country': 1}
print(Song.artist_count)  # {'Jay-Z': 2, 'Queen': 1, 'Johnny Cash': 1}

