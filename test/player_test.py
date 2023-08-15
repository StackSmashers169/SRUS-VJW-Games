import unittest
from app.player import Player
from app.player_node import PlayerNode


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player = Player('14', 'Soren')
        self.test_node = PlayerNode(self.test_player)

    def test_id(self):
        key = self.test_player.key
        self.assertEqual(key, '14')

    def test_player_name(self):
        test_player_name = self.test_player.player_name
        self.assertEqual(test_player_name, 'Soren')

    def test_create_node(self):
        test_player_name = self.test_player.player_name
        test_player_node = self.test_node

        key = test_player_node.key()
        self.assertEqual(key, '14')
