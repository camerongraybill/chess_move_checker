from .Piece import Piece
from ..Types import Color
from itertools import chain


class Queen(Piece):
    def __init__(self, color: Color):
        super(Queen, self).__init__(color)

    @property
    def character(self):
        return "Q"

    def get_possible_moves(self, board, my_position):
        return chain(self._get_diagonal_moves(board, my_position), self._get_hor_vert_moves(board, my_position))