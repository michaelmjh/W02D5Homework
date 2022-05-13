import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song('long tall sally', 'little richard')
        self.song_2 = Song('im so excited', 'ponter sisters')

        self.guest_1 = Guest('ethan', 10, self.song_1)
        self.guest_2 = Guest('pamela', 0, self.song_2)

        self.room_1 = Room('oldies', 5, 5)


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

    def test_check_in_guest_space_available(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.guests))
    
    def test_check_in_guest_no_space_available(self):
        for _ in range(6):
            self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(5, len(self.room_1.guests))

    def test_add_song(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))

    def test_remove_song(self):
        self.room_1.add_song(self.song_1)
        self.room_1.remove_song(self.song_1)
        self.assertEqual(0, len(self.room_1.songs))

    def test_play_song(self):
        self.room_1.add_song(self.song_1)
        
        self.assertEqual("Woohoo", self.guest_1.react_to_song(self.song_1))


