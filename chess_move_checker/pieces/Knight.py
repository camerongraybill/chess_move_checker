from .Piece import Piece
from ..Types import Color


class Knight(Piece):
    def __init__(self, color: Color):
        super(Knight, self).__init__(color)

    @property
    def character(self):
        return "N"

    def get_possible_moves(self, board, my_position):
        return self._get_l_moves(board, my_position)

    def get_valid_moves(self, board, my_position):
        for move in self.get_possible_moves(board, my_position):
            if self._opponents_or_empty(move.end) and self._won_or_safe(move.applied_state):
                yield move

