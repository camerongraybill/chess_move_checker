from .Piece import Piece
from ..Types import Color


class King(Piece):
    def __init__(self, color: Color):
        super(King, self).__init__(color)

    @property
    def character(self):
        return "K"

    def get_possible_moves(self, board, my_position):
        for move in self._get_one_move_away(board, my_position):
            if ((move.end.value and move.end.value.color != self.color) or not move.end.value) and not self._am_i_in_check(board.apply_move_copy(move)):
                yield move
