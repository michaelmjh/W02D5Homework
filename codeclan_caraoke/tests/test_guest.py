import unittest
from src.bar import Bar
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

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

    def test_check_can_afford_entry_pass(self):
        self.assertEqual(True, self.guest_1.check_can_afford_entry(self.room_1))

    def test_check_can_afford_entry_fail(self):
        self.assertEqual(False, self.guest_2.check_can_afford_entry(self.room_1))

    def test_pay_entry(self):
        self.guest_1.pay_entry(self.room_1)
        
        self.assertEqual(5, self.guest_1.wallet)

    def test_react_to_song_pass(self):
        self.room_1.add_song(self.song_1)

        self.assertEqual("Woohoo", self.guest_1.react_to_song(self.room_1.songs))

    def test_react_to_song_fail(self):
        self.room_1.add_song(self.song_1)
        
        self.assertIsNone(self.guest_2.react_to_song(self.room_1.songs))
