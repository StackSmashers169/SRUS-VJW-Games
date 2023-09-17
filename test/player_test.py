import unittest

import argon2.exceptions

from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player_14 = Player('14', 'Soren', 'I_remembered_it', 65)
        self.test_player_101 = Player('101', 'Bryden', 'I_forgot_it', 71)
        self.test_player_71 = Player('71', 'Stuart', 'was_hacked_yesterday', 65)
        self.test_player_86 = Player('86', 'Owen', 'Make_up', 81)
        self.test_player_93 = Player('93', 'Gladston', 'The_numbers', 77)
        self.test_node_14 = PlayerNode(self.test_player_14)
        self.test_node_101 = PlayerNode(self.test_player_101)
        self.test_node_71 = PlayerNode(self.test_player_71)
        self.test_node_86 = PlayerNode(self.test_player_86)
        self.test_node_93 = PlayerNode(self.test_player_93)
        self.test_list = PlayerList()

        # list to be sorted
        self.sorted_player_list = []

    def test_id(self):
        key = self.test_player_14.key
        self.assertEqual(key, '14')

    def test_player_name(self):
        test_player_name = self.test_player_14.player_name
        self.assertEqual(test_player_name, 'Soren')

    def test_create_node(self):
        key = self.test_node_101.next
        self.assertIsNone(key)

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

    def test_correct_password(self):
        verification = self.test_player_14.verify_password('I_remembered_it')
        self.assertIs(verification, True)

    def test_incorrect_password(self):
        verification = self.test_player_71.verify_password('I_remembered_it')
        self.assertIs(verification, False)

    def test_equal_score(self):
        self.assertIs((self.test_player_14 == self.test_player_71), True)

    def test_higher_score(self):
        self.assertIs((self.test_player_101 > self.test_player_14), True)

    def test_lower_score(self):
        self.assertIs(self.test_player_71 < self.test_player_101, True)

    def test_merge_sort(self):
        self.sorted_player_list.append(self.test_player_101)
        self.sorted_player_list.append(self.test_player_14)
        self.sorted_player_list.append(self.test_player_71)
        self.sorted_player_list.append(self.test_player_86)
        self.sorted_player_list.append(self.test_player_93)

        start = 0
        end = len(self.sorted_player_list) - 1
        expected_list = [self.test_player_86, self.test_player_93, self.test_player_101, self.test_player_14,
                         self.test_player_71]

        Player.divide_list(self.sorted_player_list, start, end)

        self.assertEqual(self.sorted_player_list, expected_list)
