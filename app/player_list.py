from typing import List, Any, Optional
from player_node import PlayerNode
from player import Player


class PlayerList:
    def __init__(self, player_list: List[Any] = None):
        self.head: Optional[Any] = None
        self.tail: Optional[Any] = None

    def append_head(self, player_data: Player):
        new_player_node = PlayerNode(player_data)

        """set new player node as new head and tail if list is empty"""
        if self.head is None:
            self.head = new_player_node
            self.tail = new_player_node
            new_player_node.previous = None
        else:
            """ make new_player_node.next point to current head, the current head previous point to
             new node and then make self.head point to the new node."""
            new_player_node.next = self.head
            self.head.previous = new_player_node
            self.head = new_player_node

    def append_tail(self, player_data: Player):
        new_player_node = PlayerNode(player_data)

        """if linked list is empty, then set head and tail as new player node"""
        if self.head is None:
            self.append_head(player_data)
        else:
            """make new_player_node.next point to current tail, the current head next is none"""
            new_player_node.previous = self.tail
            self.tail.next = new_player_node
            self.tail = new_player_node

    def remove_head(self):
        """if head is empty then raise empty list exception"""
        if self.head is None:
            raise Exception("List is empty")

    def remove_tail(self):
        """ if tail is empty then raise empty list exception"""
        if self.tail is None:
            raise Exception("List is empty")

