import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.current_player = Player('14', 'Soren')

    def test_id(self):
        key = self.current_player.key
        self.assertEqual(key, '14')

    def test_player_name(self):
        current_player_name = self.current_player.player_name
        self.assertEqual(current_player_name, 'Soren')
