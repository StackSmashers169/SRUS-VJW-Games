import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player = Player('14', 'Soren')
        self.test_node = PlayerNode(self.test_player)
        self.test_list = PlayerList()

    def test_id(self):
        key = self.test_player.key
        self.assertEqual(key, '14')

    def test_player_name(self):
        test_player_name = self.test_player.player_name
        self.assertEqual(test_player_name, 'Soren')

    def test_create_node(self):
        test_player = Player('101', 'Bryden')
        test_player_node = PlayerNode(test_player)

        key = test_player_node.next
        self.assertEqual(key, None)

    def test_append_node(self):
        """tests appending node at head and tail"""
        test_player_101 = Player('101', 'Bryden')
        test_player_node_101 = PlayerNode(test_player_101)

        self.test_list.append_head(test_player_node_101)
        self.test_list.append_tail(self.test_node)

        self.assertEqual(test_player_node_101.next, self.test_node)
        self.assertEqual(self.test_node.previous, test_player_node_101)
