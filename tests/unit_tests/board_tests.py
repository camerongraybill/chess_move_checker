from unittest import TestCase

from chess_move_checker.board import Board


class BoardTest(TestCase):

    def test_type_error(self):
        my_board = Board()
        with self.assertRaises(TypeError):
            _ = my_board["ab", 1]
        with self.assertRaises(TypeError):
            my_board["ab", 1] = None
