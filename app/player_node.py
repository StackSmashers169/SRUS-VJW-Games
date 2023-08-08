from app.player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._next = None
        self._previous = None

    def __str__(self):
        return f'Current player name: {self._player.get_player_name()}, ID: {self._player.get_unique_id()}'

    def get_player_info(self, player: Player):
        return str(player)

    @property
    def next(self):
        return self._next

    @property
    def previous(self):
        return self._previous

    # returns current player's unique id
    def key(self, player: Player):
        return player.get_unique_id()

