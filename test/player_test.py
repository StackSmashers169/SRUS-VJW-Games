import unittest
from app.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.current_player = Player('14', 'Soren')

    def test_id(self):
        unique_id = self.current_player.get_unique_id()
        self.assertEqual(unique_id, '14')

    def test_player_name(self):
        current_player_name = self.current_player.get_player_name()
        self.assertEqual(current_player_name, 'Soren')
