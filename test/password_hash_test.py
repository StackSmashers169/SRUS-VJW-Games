import unittest

import argon2.exceptions

from app.player import Player


class PasswordHashTest(unittest.TestCase):
    def setUp(self):
        self.test_player_14 = Player('14', 'Soren', 'I_remembered_it', 65)
        self.test_player_101 = Player('101', 'Bryden', 'I_forgot_it', 71)
        self.test_player_71 = Player('71', 'Stuart', 'was_hacked_yesterday', 65)

    def test_correct_password(self):
        verification = self.test_player_14.verify_password('I_remembered_it')
        self.assertIs(verification, True)

    def test_incorrect_password(self):
        verification = self.test_player_71.verify_password('I_remembered_it')
        self.assertIs(verification, False)
