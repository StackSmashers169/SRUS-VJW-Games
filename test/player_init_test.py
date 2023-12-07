import unittest

from app.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player_14 = Player('14', 'Soren', 'I_remembered_it', 65)
        self.test_player_101 = Player('101', 'Bryden', 'I_forgot_it', 71)
        self.test_player_71 = Player('71', 'Stuart', 'was_hacked_yesterday', 65)

    def test_id(self):
        key = self.test_player_14.key
        self.assertEqual(key, '14')

    def test_player_name(self):
        test_player_name = self.test_player_14.player_name
        self.assertEqual(test_player_name, 'Soren')
