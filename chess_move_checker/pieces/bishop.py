from .piece import Piece
from ..utils import MovementPatterns


class Bishop(Piece):
    @property
    def character(self):
        return "B"

    @staticmethod
    def get_possible_moves(board, my_position):
        """ Bishops can move in an X pattern, so it has the diagonal move set"""
        yield from MovementPatterns.get_diagonal_moves(board, my_position)
