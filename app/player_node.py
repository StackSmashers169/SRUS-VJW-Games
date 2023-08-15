from __future__ import annotations
from app.player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._next = None
        self._previous = None

    def __str__(self):
        return f'Current player name: {self.player_name()}, ID: {self.key()}'

    @property
    def player_name(self):
        return self._player.player_name

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    # obtains player id
    @property
    def key(self):
        return self._player.key

    # sets next node
    @next.setter
    def next(self, player_node: PlayerNode):
        self._next = player_node

    # sets previous node
    @previous.setter
    def previous(self, player_node: PlayerNode):
        self._previous = player_node
