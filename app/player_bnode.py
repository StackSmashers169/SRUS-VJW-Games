from __future__ import annotations
from typing import Optional
from app.player import Player


class PlayerBnode:
    def __init__(self, player: Player):
        self._player = player
        self._left = None
        self._right = None

    def __str__(self):
        return f'Current player name: {self.player_name}, ID: {self.key}'

    @property
    def player_name(self):
        return self._player.player_name

    @property
    def key(self):
        return self._player.key

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @left.setter
    def left(self, player_bnode: PlayerBnode):
        self._left = player_bnode

    @right.setter
    def right(self, player_bnode: PlayerBnode):
        self._right = player_bnode

