from typing import List, Any, Optional
from app.player_bnode import PlayerBNode
from app.player import Player


class PlayerBST:
    def __init__(self):
        self._root: Optional[PlayerBNode] = None

    def insert_leaf(self, player: Player, root: PlayerBNode = None):
        key = player.player_name
        new_player_b_node = PlayerBNode(player)

        if root is None:
            self._root = new_player_b_node
            return self._root

        if player.player_name < root.player_name:
            root.left = self.insert_leaf(player, root.left)
        elif player.player_name > root.player_name:
            root.right = self.insert_leaf(player, root.right)

        return root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, player_bnode: PlayerBNode):
        self._root = player_bnode


