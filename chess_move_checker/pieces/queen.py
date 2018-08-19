from .piece import Piece
from ..utils import MovementPatterns


class Queen(Piece):
    @property
    def character(self):
        return "Q"

    @staticmethod
    def get_possible_moves(board, my_position):
        """ Queens can move in a T or X shape so include both. """
        yield from MovementPatterns.get_diagonal_moves(board, my_position)
        yield from MovementPatterns.get_hor_vert_moves(board, my_position)
