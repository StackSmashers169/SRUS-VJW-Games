
class Player:
    def __init__(self, unique_id: str, player_name: str):
        self._key = unique_id
        self._player_name = player_name

    def __str__(self):
        return f'Player name: {self.player_name}, Player UID: {self.key}'

    @property
    def key(self):
        return self._key

    @property
    def player_name(self):
        return self._player_name


