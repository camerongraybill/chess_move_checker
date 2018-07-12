from .Piece import Piece
from ..Types import Color


class Pawn(Piece):
    def __init__(self, color: Color):
        super(Pawn, self).__init__(color)

    @property
    def character(self):
        return "P"

    def get_possible_moves(self, board, my_position):
        y_position = my_position.location[1] + my_position.value.color.direction
        current_x_position = my_position.location[0]
        try:
            pos = board[current_x_position - 1, y_position]
            m = board.Move(my_position, pos)
            if pos.value and pos.value.color != self.color and not self._am_i_in_check(board.apply_move_copy(m)):
                yield m
        except KeyError:
            pass
        try:
            pos = board[current_x_position, y_position]
            m = board.Move(my_position, pos)
            if pos.value.color != self.color and not pos.value:
                yield m
        except KeyError:
            pass
        try:
            pos = board[current_x_position + 1, y_position]
            m = board.Move(my_position, pos)
            if pos.value and pos.value.color != self.color and not self._am_i_in_check(board.apply_move_copy(m)):
                yield m
        except KeyError:
            pass
