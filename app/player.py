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

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Player):
            return self._score >= other.score

        return False

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Player):
            return self._score <= other.score

        return False

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Player):
            return self._player_name < other.player_name
        return False

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Player):
            return self._player_name > other.player_name
        return False

    # returns the key(ID) of the current player

    @property
    def key(self):
        return self._key

    # returns the name of the current player.
    @property
    def player_name(self):
        return self._player_name

    @player_name.setter
    def player_name(self, player_name: str):
        self._player_name = player_name

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

    @staticmethod
    def divide_list(player_list: list, start: int, end: int):
        # param: player_list of type any (preferably object type Player), start point and end point
        # the purposes of this method is to recursively split the player_list into sections
        # the actual list itself isn't split literally, but each call in td_merge will only cover the index range of
        # each section.
        if start >= end:
            return

        mid = start + (end - start) // 2
        Player.divide_list(player_list, start, mid)
        Player.divide_list(player_list, mid + 1, end)
        Player.td_merge(player_list, start, mid, end)

    @staticmethod
    def td_merge(player_list: list, start: int, mid: int, end: int):
        # param: player_list type any (preferably object type Player), start(int) - start of the section
        # mid(int) - used to calculate left and right run lengths, end(int) - end of the section.
        # td stands for top down, so top down merge, which is the technical term for the recursive merge sort method
        # this kind of sort will compare element indexes within the section passed to this function
        # and sort them based on sort criteria, for this example the higher element will go in front.

        left_total = mid - start + 1  # total elements on left side of split
        right_total = end - mid  # total elements on the right side of split

        left = []
        right = []

        for i in range(left_total):
            left.append(player_list[start + i])
        for j in range(right_total):
            right.append(player_list[mid + 1 + j])

        left_index = 0  # left tracking index
        right_index = 0  # right tracking index
        main_index = start  # tracking index for main player list we are trying to sort

        while left_index < left_total and right_index < right_total:
            if left[left_index] >= right[right_index]:
                player_list[main_index] = left[left_index]
                left_index = left_index + 1
            else:
                player_list[main_index] = right[right_index]
                right_index = right_index + 1

            main_index = main_index + 1

        # insert the remaining items
        while left_index < left_total:
            player_list[main_index] = left[left_index]
            main_index = main_index + 1
            left_index = left_index + 1

        while right_index < right_total:
            player_list[main_index] = right[right_index]
            main_index = main_index + 1
            right_index = right_index + 1
