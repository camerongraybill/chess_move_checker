from .Piece import Piece
from ..Types import Color


class Bishop(Piece):
    def __init__(self, color: Color):
        super(Bishop, self).__init__(color)

    @property
    def character(self):
        return "B"

    def get_possible_moves(self, board, my_position):
        return self._get_diagonal_moves(board, my_position)
