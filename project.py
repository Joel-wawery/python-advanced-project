class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

class Song:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.songs = []

    def add_song(self, title, year):
        song = Song(title, self.artist, year)
        self.songs.append(song)
        self.artist.add_song(song)

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def list_songs(self):
        return [f"{song.title} by {song.artist.name} ({song.year})" for song in self.songs]


artist = Artist("Kim walker smith")


album = Album("i dont have much", artist)


album.add_song("at the centre", 2017)
album.add_song("worthy", 2010)


song = Song("coming", artist, 2018)
artist.add_song(song)

playlist = Playlist("bethel world",)


for song in album.songs:
    playlist.add_song(song)


playlist.add_song(song)


print("Songs in the playlist:")
for song in playlist.list_songs():
    print(song)


print("\nSongs by The hillside:")
for song in artist.songs:
    print(f"{song.title} ({song.year})")


artist2 = Artist("david funk")
album2 = Album("David laid", artist2)
album2.add_song("hold", 2013)
album2.add_song("Tend", 2016)

song2 = Song("Wish You Were Here", artist2, 2016)
artist2.add_song(song2)

playlist2 = Playlist("Another measure")
for song in album2.songs:
    playlist2.add_song(song)
playlist2.add_song(song2)

print("\nSongs in the Another measure playlist:")
for song in playlist2.list_songs():
    print(song)

print("\nSongs by david funk:")
for song in artist2.songs:
    print(f"{song.title} ({song.year})")
      
