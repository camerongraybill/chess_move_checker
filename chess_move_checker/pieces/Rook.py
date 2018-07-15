from .Piece import Piece
from ..Types import Color


class Rook(Piece):
    def __init__(self, color: Color):
        super(Rook, self).__init__(color)

    @property
    def character(self):
        return "R"

    def get_possible_moves(self, board, my_position):
        return self._get_hor_vert_moves(board, my_position)
