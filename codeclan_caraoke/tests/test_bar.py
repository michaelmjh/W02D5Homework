import unittest
from src.bar import Bar
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestBar(unittest.TestCase):

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

    def test_increase_till(self):
        self.bar_1.increase_till(self.bar_1.rooms[0])
        self.assertEqual(105, self.bar_1.till)

    def test_check_in_guest_space_available(self):
        self.bar_1.check_in_guest(self.room_1, self.guest_1)
        
        self.assertEqual(1, len(self.room_1.guests))
        self.assertEqual(105, self.bar_1.till)
    
    def test_check_in_guest_guest_already_checked_in(self):
        self.bar_1.check_in_guest(self.room_1, self.guest_1)
        self.bar_1.check_in_guest(self.room_1, self.guest_1)
        
        self.assertEqual(1, len(self.room_1.guests))
        self.assertEqual(105, self.bar_1.till)

    def test_check_in_guest_no_space_available(self):
        self.bar_1.check_in_guest(self.room_1, self.guest_1)
        self.bar_1.check_in_guest(self.room_1, self.guest_3)
        self.bar_1.check_in_guest(self.room_1, self.guest_4)
        self.bar_1.check_in_guest(self.room_1, self.guest_5)
        self.bar_1.check_in_guest(self.room_1, self.guest_6)
        self.bar_1.check_in_guest(self.room_1, self.guest_7)

        self.assertEqual(5, len(self.room_1.guests))
        self.assertEqual(125, self.bar_1.till)
        self.assertEqual(5, self.guest_1.wallet)

    def test_check_in_guest_guest_cant_afford(self):
        self.bar_1.check_in_guest(self.room_1, self.guest_2)
        
        self.assertEqual(0, len(self.room_1.guests))
        self.assertEqual(100, self.bar_1.till)
        self.assertEqual(3, self.guest_2.wallet)

    def test_check_out_guest(self):
        self.bar_1.check_in_guest(self.room_1, self.guest_1)
        self.bar_1.check_out_guest(self.room_1, self.guest_1)

        self.assertEqual(0, len(self.room_1.guests))
