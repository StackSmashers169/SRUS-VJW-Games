import unittest
from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player_14 = Player('14', 'Soren')
        self.test_player_101 = Player('101', 'Bryden')
        self.test_player_71 = Player('71', 'Stuart')
        self.test_node_14 = PlayerNode(self.test_player_14)
        self.test_node_101 = PlayerNode(self.test_player_101)
        self.test_node_71 = PlayerNode(self.test_player_71)
        self.test_list = PlayerList()

    def test_id(self):
        key = self.test_player_14.key
        self.assertEqual(key, '14')

    def test_player_name(self):
        test_player_name = self.test_player_14.player_name
        self.assertEqual(test_player_name, 'Soren')

    def test_create_node(self):
        test_player = Player('101', 'Bryden')
        test_player_node = PlayerNode(test_player)

        key = test_player_node.next
        self.assertEqual(key, None)

    def test_append_node(self):
        """tests appending node at head and tail"""

        self.test_list.append_head(self.test_node_101)
        self.test_list.append_tail(self.test_node_14)

        self.assertEqual(self.test_node_14, self.test_node_14)
        self.assertEqual(self.test_node_14.previous, self.test_node_101)

    def test_empty_list_exception(self):
        """tests removing from head"""
        with self.assertRaises(IndexError):
            self.test_list.remove_head()

    def test_remove_head(self):
        self.test_list.append_head(self.test_node_14)
        self.test_list.append_head(self.test_node_71)
        self.test_list.append_head(self.test_node_101)

        removed_node = self.test_list.remove_head()
        self.assertEqual(removed_node, self.test_node_101)
        self.assertEqual(self.test_node_71.next, self.test_node_14)
        self.assertEqual(self.test_node_14.previous, self.test_node_71)

    def test_remove_tail(self):
        self.test_list.append_tail(self.test_node_101)
        self.test_list.append_tail(self.test_node_71)
        self.test_list.append_tail(self.test_node_14)

        removed_node = self.test_list.remove_tail()
        self.assertEqual(removed_node, self.test_node_14)
        self.assertEqual(self.test_node_71.previous, self.test_node_101)
        self.assertEqual(self.test_node_101.next, self.test_node_71)

    def test_remove_by_key(self):
        self.test_list.append_head(self.test_node_71)
        self.test_list.append_head(self.test_node_101)
        self.test_list.append_tail(self.test_node_14)

        removed_none = self.test_list.remove_specific_node('0')
        self.assertEqual(removed_none, None)

        removed_71 = self.test_list.remove_specific_node('71')
        self.assertEqual(removed_71, self.test_node_71)
        