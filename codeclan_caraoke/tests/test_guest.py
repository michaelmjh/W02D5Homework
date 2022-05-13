import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song('long tall sally', 'little richard')
        self.song_2 = Song('im so excited', 'ponter sisters')

        self.guest_1 = Guest('ethan', 10, self.song_1)
        self.guest_2 = Guest('pamela', 0, self.song_2)

    def test_check_can_afford_entry_pass(self):
        self.assertEqual(True, self.guest_1.check_can_afford_entry())

    def test_check_can_afford_entry_fail(self):
        self.assertEqual(False, self.guest_2.check_can_afford_entry())

    def test_pay_entry(self):
        self.guest_1.pay_entry()
        self.assertEqual(5, self.guest_1.wallet)

    def test_react_to_song_pass(self):
        self.assertEqual("Woohoo", self.guest_1.react_to_song(self.song_1))

    def test_react_to_song_fail(self):
        self.assertIsNone(self.guest_2.react_to_song(self.song_1))
