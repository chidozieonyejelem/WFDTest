import random

#Artist class
class Artist:
    def __init__(self, name, dob, country):
        self.name = name
        self.dob = dob
        self.country = country
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)
        print(f"Added album '{album.title}' to artist '{self.name}'")

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added song '{song.title}' to artist '{self.name}'")

    def display_info(self):
        print(f"Artist: {self.name}, DoB: {self.dob}, Country: {self.country}")
        print(f"Albums = {len(self.albums)}: {[a.title for a in self.albums]}")
        print(f"Songs = {len(self.songs)}: {[s.title for s in self.songs]}")

#Song class
class Song:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year

    def display_info(self):
        print(f"Song: {self.title}, Artist: {self.artist_name}, Year: {self.year}")

#Album class
class Album:
    def __init__(self, title, artist_name, year):
        self.title = title
        self.artist_name = artist_name
        self.year = year
        self.songs = []

    def add_song(self, title, year):
        song = Song(title, self.artist_name, year)
        self.songs.append(song)
        print(f"Added song '{song.title}' to album '{self.title}'")
        return song

    def display_info(self):
        print(f"Album: {self.title}, Artist: {self.artist_name}, Year: {self.year}")
        print(f"Songs = {len(self.songs)}:")
        for song in self.songs:
            print(f"{song.title} - {song.year}")

#Playlist class
class Playlist:
    def __init__(self, title):
        self.title = title
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def print_all_songs(self):
        print(f"\nPlaylist: {self.title}")
        for i, song in enumerate(self.songs, 1):
            print(f"{song.title} - {song.artist_name}, {song.year}")

    def sort_playlist(self, order='ASC'):
        reverse = (order == 'DES')
        self.songs.sort(key=lambda s: s.title, reverse=reverse)
        print(f"Playlist sorted in {'descending' if reverse else 'ascending'} order.")

    def shuffle_playlist(self):
        random.shuffle(self.songs)
        print("Playlist shuffled.")

#Creates an artist
taylor = Artist("Taylor Swift", "1989-12-13", "USA")

#Creates an album
fearless = Album("Fearless", "Taylor Swift", 2008)

#Creates a song for an artist
song1 = Song("Fifteen", "Taylor Swift", 2008)
song2 = Song("Love Story", "Taylor Swift", 2008)
song3 = Song("Hey Stephen", "Taylor Swift", 2008)
song4 = Song("White Horse", "Taylor Swift", 2014)

#Adds a song to an album
fearless.add_song("Fifteen", 2008)
fearless.add_song("Love Story", 2008)

#Updates the artist
taylor.add_album(fearless)
taylor.add_song(song1)
taylor.add_song(song2)
taylor.add_song(song3)
taylor.add_song(song4)

#Creates a playlist
playlist = Playlist("Taylor Swift Playlist")

#Adds all songs from the album to the playlist
for song in fearless.songs:
    playlist.add_song(song)

#Displays all the output information
print("\nArtist Information")
taylor.display_info()

print("\nAlbum Information")
fearless.display_info()

print("\nPlaylist Information")
playlist.print_all_songs()

print("\nSong Information")
song1.display_info()
song2.display_info()

print("\nSort Playlist in ASC order")
playlist.sort_playlist('ASC')
playlist.print_all_songs()

print("\nSort Playlist in DES order")
playlist.sort_playlist('DES')
playlist.print_all_songs()

print("\nShuffle Playlist")
playlist.shuffle_playlist()
playlist.print_all_songs()