from .Piece import Piece
from ..Types import Color
from itertools import chain
from ..Utils import MovementPatterns


class Queen(Piece):
    def __init__(self, color: Color):
        super(Queen, self).__init__(color)

    @property
    def character(self):
        return "Q"

    @staticmethod
    def get_possible_moves(board, my_position):
        return chain(MovementPatterns.get_diagonal_moves(board, my_position),
                     MovementPatterns.get_hor_vert_moves(board, my_position))
