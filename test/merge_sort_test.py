import unittest

from app.player import Player


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        self.test_player_14 = Player('14', 'Soren', 'I_remembered_it', 65)
        self.test_player_101 = Player('101', 'Bryden', 'I_forgot_it', 71)
        self.test_player_71 = Player('71', 'Stuart', 'was_hacked_yesterday', 65)
        self.test_player_86 = Player('86', 'Owen', 'Make_up', 81)
        self.test_player_93 = Player('93', 'Gladston', 'The_numbers', 77)
        self.sorted_player_list = []

    def test_equal_score(self):
        self.assertIs((self.test_player_14 == self.test_player_71), True)

    def test_higher_score(self):
        self.assertIs((self.test_player_101 >= self.test_player_14), True)

    def test_lower_score(self):
        self.assertIs(self.test_player_71 <= self.test_player_101, True)

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
