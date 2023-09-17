from typing import List, Any, Optional
from app.player_node import PlayerNode


class PlayerList:
    # a player list holds a list of a player nodes
    def __init__(self, player_list: List[Any] = None):
        self.head: Optional[PlayerNode] = None
        self.tail: Optional[PlayerNode] = None

        if player_list:
            for player_node in player_list:
                self.append_head(player_node)

    def append_head(self, player_node: PlayerNode):

        # set new player node as new head and tail if list is empty
        if self.head is None:
            self.head = player_node
            self.tail = player_node
            player_node.previous = None
        else:
            # make new_player_node.next point to current head, the current head previous point to
            # new node and then make self.head point to the new node
            player_node.next = self.head
            self.head.previous = player_node
            self.head = player_node

    def append_tail(self, player_node: PlayerNode):

        # if linked list is empty, then set head and tail as new player node"""
        if self.head is None:
            self.append_head(player_node)

        else:
            # make new_player_node.next point to current tail, the current head next is none"""
            player_node.previous = self.tail
            self.tail.next = player_node
            self.tail = player_node

    def remove_head(self):
        # removes head of the linked list and returns removed node
        # if head is empty then raise empty list exception

        if self.head is None:
            raise IndexError("List is empty")

        if self.head.next is None:
            removed_node = self.head
            self.head = None
            return removed_node

        removed_node = self.head
        self.head = self.head.next
        return removed_node

    def remove_tail(self):
        # removes tail and returns removed tail.  If tail is empty then raise empty list exception
        if self.head is None:
            raise IndexError("List is empty")

        """if the list only has 1 node remove it then return"""
        if self.head.next is None:
            removed_node = self.tail
            self.remove_head()
            return removed_node

        removed_node = self.tail
        self.tail = self.tail.previous
        return removed_node

    def remove_specific_node(self, key: str):

        # removes a player from the list by key and then returns the node that was removed
        # :param key: str - the id of the player we want to remove from the list.

        if self.head is None:
            raise IndexError("List is empty")

        """traverse the list until you reach a node that has a matching key"""
        current_player = self.head
        while current_player is not None:
            if key == self.head.key:
                removed_node = self.head
                self.remove_head()
                return removed_node
            elif key == self.tail.key:
                removed_node = self.tail
                self.remove_tail()
                return removed_node
            elif key == current_player.key:
                current_player.previous.next = current_player.next
                current_player.next.previous = current_player.previous
                return current_player

            current_player = current_player.next

        # if we reached here, then that means no key was found
        return None

    def display(self, forward=True):
        # displays the list of nodes currently in the player list
        if forward:
            current_node = self.head
            while current_node is not None:
                print(str(current_node))
                current_node = current_node.next
        else:
            current_node = self.tail
            while current_node is not None:
                print(str(current_node))
                current_node = current_node.previous



