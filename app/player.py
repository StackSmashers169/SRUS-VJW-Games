import argon2.exceptions
from argon2 import PasswordHasher


class Player:
    def __init__(self, unique_id: str, player_name: str, password: str):
        self._key = unique_id
        self._player_name = player_name
        self.password = password
        self._hashed_password = ''
        self.add_password(self.password)

    def __str__(self):
        return f'Player name: {self.player_name}, Player UID: {self.key}'

    @property
    def key(self):
        return self._key

    @property
    def player_name(self):
        return self._player_name

    # both methods below use the pypi package argon2, this package was installed using the command:
    # python -Im pip install argon2-cffi
    def add_password(self, password: str):
        hasher = PasswordHasher()
        self._hashed_password = hasher.hash(password)

    def verify_password(self, password: str):
        hasher = PasswordHasher()
        try:
            hasher.verify(self._hashed_password, password)
            return True
        except argon2.exceptions.VerifyMismatchError:
            return False
