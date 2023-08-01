
class Player:
    def __init__(self, unique_id: str, player_name: str):
        self.unique_id = unique_id
        self.player_name = player_name

    def __str__(self):
        return f'Player name: {self.player_name}, Player UID: {self.unique_id}'

    def get_unique_id(self):
        return self.unique_id

    def get_player_name(self):
        return self.player_name


