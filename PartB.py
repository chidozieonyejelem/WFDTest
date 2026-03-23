import unittest
from PartA import Song, Album, Artist, Playlist

"""Checks if an object is an instance of a class"""
class TestInstanceOf(unittest.TestCase):
    def test_artist_is_instance(self):
        artist = Artist("Taylor Swift", "1989-12-13", "USA")
        self.assertIsInstance(artist, Artist)

    def test_song_is_instance(self):
        song = Song("Fearless", "Taylor Swift", 2008)
        self.assertIsInstance(song, Song)

    def test_album_is_instance(self):
        album = Album("Fearless", "Taylor Swift", 2008)
        self.assertIsInstance(album, Album)

    def test_playlist_is_instance(self):
        playlist = Playlist("My Playlist")
        self.assertIsInstance(playlist, Playlist)

"""Checks if an object is not an instance of a class"""
class TestNotInstanceOf(unittest.TestCase):
    def test_artist_not_playlist(self):
        artist = Artist("Taylor Swift", "1989-12-13", "USA")
        self.assertNotIsInstance(artist, Playlist)

    def test_song_not_album(self):
        song = Song("Fearless", "Taylor Swift", 2008)
        self.assertNotIsInstance(song, Album)

    def test_album_not_artist(self):
        album = Album("Fearless", "Taylor Swift", 2008)
        self.assertNotIsInstance(album, Artist)

    def test_playlist_not_song(self):
        playlist = Playlist("My Playlist")
        self.assertNotIsInstance(playlist, Song)

"""Checks if two objects are identical or unidentical but similar"""
class TestObjectIdentity(unittest.TestCase):
    def test_identical_objects(self):
        song = Song("Love Story", "Taylor Swift", 2008)
        same_song = song
        self.assertIs(song, same_song)

    def test_similar_but_not_identical(self):
        song1 = Song("Love Story", "Taylor Swift", 2008)
        song2 = Song("Love Story", "Taylor Swift", 2008)
        self.assertIsNot(song1, song2)

"""Checks if add song and album methods are working"""
class testAddMethods(unittest.TestCase):
    def test_artist_add_song(self):
        artist = Artist("Taylor Swift", "1989-12-13", "USA")
        song = Song("Love Story", "Taylor Swift", 2008)
        artist.add_song(song)
        self.assertIn(song, artist.songs)

    def test_artist_add_album(self):
        artist = Artist("Taylor Swift", "1989-12-13", "USA")
        album = Album("Fearless", "Taylor Swift", 2008)
        artist.add_album(album)
        self.assertIn(album, artist.albums)

    def test_album_add_song(self):
        album = Album("Fearless", "Taylor Swift", 2008)
        album.add_song("Fearless", 2008)
        self.assertEqual(len(album.songs), 1)
        self.assertEqual(album.songs[0].title, "Fearless")

    def test_playlist_add_song(self):
        playlist = Playlist("My Playlist")
        song = Song("Fifteen", "Taylor Swift", 2014)
        playlist.add_song(song)
        self.assertIn(song, playlist.songs)

"""Checks if playlist sorting methods are working"""
class TestPlaylistSorting(unittest.TestCase):
    def test_sort_ascending(self):
        playlist = Playlist("My Playlist")
        playlist.add_song(Song("Love Story", "Taylor Swift", 2008))
        playlist.add_song(Song("Fearless", "Taylor Swift", 2008))
        playlist.add_song(Song("Fifteen", "Taylor Swift", 2008))
        playlist.sort_playlist('ASC')
        titles = [s.title for s in playlist.songs]
        self.assertEqual(titles, sorted(titles))

    def test_sort_descending(self):
        playlist = Playlist("My Playlist")
        playlist.add_song(Song("Love Story", "Taylor Swift", 2008))
        playlist.add_song(Song("White Horse", "Taylor Swift", 2008))
        playlist.add_song(Song("Fifteen", "Taylor Swift", 2008))
        playlist.sort_playlist('DES')
        titles = [s.title for s in playlist.songs]
        self.assertEqual(titles, sorted(titles, reverse=True))

    def test_shuffle_playlist(self):
        playlist = Playlist("My Playlist")
        playlist.add_song(Song("Love Story", "Taylor Swift", 2008))
        playlist.add_song(Song("White Horse", "Taylor Swift", 2008))
        playlist.add_song(Song("Fifteen", "Taylor Swift", 2008))
        original_titles = [s.title for s in playlist.songs]
        for _ in range(10):
            playlist.shuffle_playlist()
            if [s.title for s in playlist.songs] != original_titles:
                break
        self.assertEqual(sorted([s.title for s in playlist.songs]), sorted(original_titles))

if __name__ == '__main__':
    unittest.main()