from typing import List, Any, Optional
from app.player_bnode import PlayerBNode
from app.player import Player


class PlayerBST:
    def __init__(self):
        self._root: Optional[PlayerBNode] = None

    def insert_leaf(self, root: PlayerBNode, player: Player):
        key = player.player_name
        new_player_b_node = PlayerBNode(player)

        if root is None:
            return new_player_b_node

        if player.player_name < root.player_name:
            root.left = self.insert_leaf(root.left, player)
        elif player.player_name > root.player_name:
            root.right = self.insert_leaf(root.right, player)

        return root

