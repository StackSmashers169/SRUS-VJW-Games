from typing import Optional
from app.player_bnode import PlayerBNode
from app.player import Player


class PlayerBST:
    def __init__(self):
        self._root: Optional[PlayerBNode] = None
        self._balancer_list = []

    def insert_leaf(self, player: Player, root: PlayerBNode = None):
        key = player.player_name
        if root is None:
            root = PlayerBNode(player)
            return root

        while key == root.player.player_name:
            print("This name already exists, please choose another")
            player.player_name = input()
            key = player.player_name

        if player.player_name < root.player.player_name:
            root.left = self.insert_leaf(player, root.left)
        elif player.player_name > root.player.player_name:
            root.right = self.insert_leaf(player, root.right)

        return root

    def search_tree(self, root: PlayerBNode, key: str):
        if root is None or root.player.player_name == key:
            return root

        if root.player.player_name < key:
            return self.search_tree(root.right, key)

        return self.search_tree(root.left, key)

    # helper method that uses DFS inorder traversal
    # to collect all nodes into balancing list.
    def collect_nodes(self, root: PlayerBNode = None):
        if root:
            # traverse left side
            self._balancer_list = (self.collect_nodes(root.left))

            # collect node into list
            self._balancer_list.append(root.player)

            # traverse right side
            self._balancer_list = (self.collect_nodes(root.right))

        return self._balancer_list

    # selects the middle element to be the root in the tree
    # so that we can create a balanced binary tree instead
    def balance_tree(self, balancer_list: list, start: int, end: int, root: PlayerBNode = None):
        # find the middle of the list and set it as main root

        if start >= end:
            # when we reach the last element add it before exiting recursion loop.
            if start == (len(balancer_list) - 1):
                self.insert_leaf(balancer_list[start], root)
            return

        mid = start + (end - start) // 2

        if root is None:
            root = self.insert_leaf(balancer_list[mid])
            self._root = root

        if balancer_list[mid] < root.player:
            self.insert_leaf(balancer_list[mid], root)
        elif balancer_list[mid] > root.player:
            self.insert_leaf(balancer_list[mid], root)

        self.balance_tree(balancer_list, start, mid, root)
        self.balance_tree(balancer_list, mid + 1, end, root)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, player_bnode: PlayerBNode):
        self._root = player_bnode


# testing the functionality of the tree balancer
if __name__ == '__main__':
    test_player_14 = Player('14', 'Soren', 'I_remembered_it', 65)
    test_player_101 = Player('101', 'Bryden', 'I_forgot_it', 71)
    test_player_71 = Player('71', 'Stuart', 'I_was_hacked_yesterday', 65)
    test_player_86 = Player('86', 'Owen', 'Climbing_a', 81)
    test_player_93 = Player('93', 'Gladston', 'binary_tree', 77)
    test_player_37 = Player('37', 'Rice', 'tree_climbing', 69)
    test_tree = PlayerBST()

    # inserting into the tree
    test_root = test_tree.insert_leaf(test_player_14)
    test_tree.insert_leaf(test_player_101, test_root)
    test_tree.insert_leaf(test_player_71, test_root)
    test_tree.insert_leaf(test_player_86, test_root)
    test_tree.insert_leaf(test_player_93, test_root)
    test_tree.insert_leaf(test_player_37, test_root)
    # print unbalanced tree

    # collect tree into array
    test_list = test_tree.collect_nodes(test_root)
    test_start = 0
    test_end = len(test_list) - 1
    test_tree.balance_tree(test_list, test_start, test_end)

    print(test_tree.search_tree(test_tree.root, 'Stuart'))

