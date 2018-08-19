from .Piece import Piece
from ..Types import Color
from ..Utils import MovementPatterns


class Rook(Piece):
    def __init__(self, color: Color):
        super(Rook, self).__init__(color)

    @property
    def character(self):
        return "R"

    @staticmethod
    def get_possible_moves(board, my_position):
        """ Rooks move in a T formation, or horizontal and vertical moves """
        yield from MovementPatterns.get_hor_vert_moves(board, my_position)
