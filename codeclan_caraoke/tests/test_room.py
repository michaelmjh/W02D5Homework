import unittest
from src.bar import Bar
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song('long tall sally', 'little richard')
        self.song_2 = Song('im so excited', 'ponter sisters')

        self.guest_1 = Guest('a', 10, self.song_1)
        self.guest_2 = Guest('b', 3, self.song_2)
        self.guest_3 = Guest('c', 10, self.song_1)
        self.guest_4 = Guest('d', 10, self.song_2)
        self.guest_5 = Guest('e', 10, self.song_1)
        self.guest_6 = Guest('f', 10, self.song_2)
        self.guest_7 = Guest('g', 10, self.song_2)

        self.room_1 = Room('oldies', 5, 5)
        self.room_2 = Room('rock', 10, 10)
        
        rooms = [self.room_1, self.room_2]

        self.bar_1 = Bar('ccc', 100, rooms)

    def test_check_space_available_true(self):
        self.room_1.add_guest(self.guest_1)
        
        self.assertEqual(True, self.room_1.check_space_available())

    def test_check_space_available_false(self):
        for _ in range(5):
            self.room_1.add_guest(self.guest_1)
        
        self.assertEqual(False, self.room_1.check_space_available())

    def test_add_guest(self):
        self.room_1.add_guest(self.guest_1)
        
        self.assertEqual(1, len(self.room_1.guests))

    def test_remove_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.room_1.remove_guest(self.guest_2)
        
        self.assertEqual(1, len(self.room_1.guests))

    def test_add_song(self):
        self.room_1.add_song(self.song_1)
        
        self.assertEqual(1, len(self.room_1.songs))

    def test_add_multiple_songs(self):
        for _ in range(5):
            self.room_1.add_song(self.song_1)
            self.room_1.add_song(self.song_2)
        
        self.assertEqual(10, len(self.room_1.songs))
        
    def test_remove_song(self):
        self.room_1.add_song(self.song_1)
        self.room_1.remove_song(self.song_1)
        
        self.assertEqual(0, len(self.room_1.songs))

    def test_play_song_pass(self):
        self.room_1.add_song(self.song_1)
        self.room_2.add_song(self.song_2)

        self.assertEqual("Woohoo", self.guest_1.react_to_song(self.room_1.songs))

    def test_play_song_fail(self):
        self.room_1.add_song(self.song_2)

        self.assertEqual(None, self.guest_1.react_to_song(self.room_1.songs))

