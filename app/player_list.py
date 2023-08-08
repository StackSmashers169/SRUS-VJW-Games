from typing import List, Any, Optional
from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self, player_list: List[Any] = None):
        self.head: Optional[Any] = None

    def append_node(self, player_data: Player):
        new_player_node = PlayerNode(player_data)

        """set new player node as new head if list is empty"""
        if self.head is None:
            self.head = new_player_node
            new_player_node.previous = None
        else:
            """ make new_node.next point to current head, the current head previous point to
             new node and then make self.head point to the new node"""
            new_player_node.next = self.head
            self.head.previous = new_player_node
            self.head = new_player_node






