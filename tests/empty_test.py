from unittest import TestCase
from chess_move_checker.pieces.Piece import Piece

class DummyTest(TestCase):

    def test_me(self):
        Piece()
        self.assertTrue(1 == 1)
