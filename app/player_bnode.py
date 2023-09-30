from __future__ import annotations
from typing import Optional, Any
from app.player import Player


class PlayerBNode:
    def __init__(self, player: Player):
        self._player = player
        self._left = None
        self._right = None

    def __str__(self):
        return f'Current player name: {self.player.player_name}, ID: {self.player.key}'

    # comparison operator magic methods for less than and greater than.

    @property
    def player(self):
        return self._player

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, player_bnode: PlayerBNode):
        self._left = player_bnode

    @right.setter
    def right(self, player_bnode: PlayerBNode):
        self._right = player_bnode


