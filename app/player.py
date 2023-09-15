from typing import Any
import argon2.exceptions
from argon2 import PasswordHasher


class Player:
    def __init__(self, unique_id: str, player_name: str, password: str, score: int):
        self._key = unique_id
        self._player_name = player_name
        self.password = password
        self._hashed_password = ''
        self._score = score
        self.add_password(self.password)

    def __str__(self):
        return f'Player name: {self.player_name}, Player UID: {self.key}'

    # comparison for if players have an equal score and a tiebreaker is required.
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Player):
            return self._score == other.score

        return False

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Player):
            return self._score > other.score

        return False

    # returns the key(ID) of the current player
    @property
    def key(self):
        return self._key

    # returns the name of the current player.
    @property
    def player_name(self):
        return self._player_name

    # returns the score of the current player
    @property
    def score(self):
        return self._score

    # sets new score for current player
    @score.setter
    def score(self, score: int):
        self._score = score

    # both methods below use the pypi package argon2, this package was installed using the command:
    # python -Im pip install argon2-cffi
    def add_password(self, password: str):
        # takes a plaintext string and converts it into a hash using argon2's built in hash() function.
        hasher = PasswordHasher()
        self._hashed_password = hasher.hash(password)

    def verify_password(self, password: str):
        # takes a plaintext string and then verifies it by attempting to create a hash that matches the
        # current instance of this player's stored "hashed" password.
        hasher = PasswordHasher()
        try:
            hasher.verify(self._hashed_password, password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False
