from .Piece import Piece
from ..Types import Color
from ..Utils import MovementPatterns


class Bishop(Piece):
    def __init__(self, color: Color):
        super(Bishop, self).__init__(color)

    @property
    def character(self):
        return "B"

    @staticmethod
    def get_possible_moves(board, my_position):
        """ Bishops can move in an X pattern, so it has the diagonal move set"""
        yield from MovementPatterns.get_diagonal_moves(board, my_position)
