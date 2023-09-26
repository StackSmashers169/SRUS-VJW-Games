from typing import List, Any, Optional
from app.player_bnode import PlayerBNode
from app.player import Player


class PlayerBST:
    def __init__(self):
        self._root: Optional[PlayerBNode] = None

    def insert_leaf(self, player: Player, root: PlayerBNode = None):
        key = player.player_name
        record = []
        if self.check_duplicate(record, key):
            print("This name is already taken, please enter another name")
            player.player_name = input()

        new_player_b_node = PlayerBNode(key)

        if root is None:
            self._root = new_player_b_node
            return self._root

        if player.player_name < root.player_name:
            root.left = self.insert_leaf(player, root.left)
        elif player.player_name > root.player_name:
            root.right = self.insert_leaf(player, root.right)

        return root

    def check_duplicate(self, record: list, player_name: str):
        if not record:
            return False

        for index in record:
            if record[index] == player_name:
                return True

        return False

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, player_bnode: PlayerBNode):
        self._root = player_bnode


