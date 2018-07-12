from .Piece import Piece
from ..Types import Color


class Rook(Piece):
    def __init__(self, color: Color):
        super(Rook, self).__init__(color)

    @property
    def character(self):
        return "R"

    def get_possible_moves(self, board, my_position):
        for move in self._get_hor_vert_moves(board, my_position):
            # Check if there is anything between start position and end position
            # And make sure that we are not moving into check
            if ((move.end.value and move.end.value.color != self.color) or not move.end.value) and not any(move.traversed_pieces) and not self._am_i_in_check(board.apply_move_copy(move)):
                yield move
