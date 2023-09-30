import unittest

from app.player import Player
from app.player_bst import PlayerBST
from app.player_bnode import PlayerBNode


class TestBST(unittest.TestCase):
    def setUp(self):
        self.test_player_14 = Player('14', 'Soren', 'I_remembered_it', 65)
        self.test_player_101 = Player('101', 'Bryden', 'I_forgot_it', 71)
        self.test_player_71 = Player('71', 'Stuart', 'I_was_hacked_yesterday', 65)
        self.test_player_86 = Player('86', 'Owen', 'Climbing_a', 81)
        self.test_player_93 = Player('93', 'Gladston', 'binary_tree', 77)
        self.test_player_37 = Player('37', 'Rice', 'tree_climbing', 69)

        self.test_tree = PlayerBST()

    # tests inserting the first element into the tree.
    def test_initialize_bst(self):
        test_root = PlayerBNode(self.test_player_86)
        test_name = test_root.player_name
        self.test_tree.root = self.test_tree.insert_leaf(self.test_player_86)
        self.assertEqual(test_name, self.test_tree.root.player_name)

    # test inserting an element less than the root.
    def test_insert_left(self):
        first_node = self.test_tree.insert_leaf(self.test_player_86)
        self.test_tree.root = self.test_tree.insert_leaf(self.test_player_101, first_node)
        left_node = self.test_tree.root.left
        self.assertEqual(self.test_player_101.player_name, left_node.player_name)

    def test_insert_right(self):
        first_node = self.test_tree.insert_leaf(self.test_player_86)
        self.test_tree.root = self.test_tree.insert_leaf(self.test_player_14, first_node)
        right_node = self.test_tree.root.right
        self.assertEqual(self.test_player_14.player_name, right_node.player_name)

    def test_search_pass(self):
        root = self.test_tree.insert_leaf(self.test_player_14)
        self.test_tree.insert_leaf(self.test_player_101, root)
        self.test_tree.insert_leaf(self.test_player_71, root)
        self.test_tree.insert_leaf(self.test_player_86, root)
        self.test_tree.insert_leaf(self.test_player_93, root)
        self.test_tree.insert_leaf(self.test_player_37, root)

        found_node = self.test_tree.search_tree(root, 'Gladston')
        # search the tree
        self.assertEqual(found_node.player_name, 'Gladston')

    def test_search_fail(self):
        root = self.test_tree.insert_leaf(self.test_player_14)
        self.test_tree.insert_leaf(self.test_player_101, root)
        self.test_tree.insert_leaf(self.test_player_71, root)
        self.test_tree.insert_leaf(self.test_player_86, root)
        self.test_tree.insert_leaf(self.test_player_93, root)
        self.test_tree.insert_leaf(self.test_player_37, root)

        self.assertIsNone(self.test_tree.search_tree(root, 'None'))



