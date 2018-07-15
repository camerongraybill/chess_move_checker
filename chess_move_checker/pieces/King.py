from .Piece import Piece
from ..Types import Color


class King(Piece):
    def __init__(self, color: Color):
        super(King, self).__init__(color)

    @property
    def character(self):
        return "K"

    def get_possible_moves(self, board, my_position):
        return self._get_one_move_away(board, my_position)

