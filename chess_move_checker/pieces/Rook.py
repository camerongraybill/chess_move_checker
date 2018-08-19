from .piece import Piece
from ..utils import MovementPatterns


class Rook(Piece):
    @property
    def character(self):
        return "R"

    @staticmethod
    def get_possible_moves(board, my_position):
        """ Rooks move in a T formation, or horizontal and vertical moves """
        yield from MovementPatterns.get_hor_vert_moves(board, my_position)
