from .Piece import Piece
from ..Types import Color


class Pawn(Piece):
    def __init__(self, color: Color):
        super(Pawn, self).__init__(color)

    @property
    def character(self):
        return "P"

    def get_possible_moves(self, board, my_position):
        y_position = my_position.location[1] + self.color.direction
        current_x_position = my_position.location[0]
        for x in (-1, 0, 1):
            try:
                yield board.Move(my_position, board.get_board_location((current_x_position + x, y_position)))
            except KeyError:
                pass

    def get_valid_moves(self, board, my_position):
        y_position = my_position.location[1] + self.color.direction
        current_x_position = my_position.location[0]
        try:
            pos = board.get_board_location((current_x_position - 1, y_position))
            m = board.Move(my_position, pos)
            if pos.value and pos.value.color != self.color and self._won_or_safe(m.applied_state):
                yield m
        except KeyError:
            pass
        try:
            pos = board.get_board_location((current_x_position, y_position))
            m = board.Move(my_position, pos)
            if not pos.value and self._won_or_safe(m.applied_state):
                yield m
        except KeyError:
            pass
        try:
            pos = board.get_board_location((current_x_position + 1, y_position))
            m = board.Move(my_position, pos)
            if pos.value and pos.value.color != self.color and self._won_or_safe(m.applied_state):
                yield m
        except KeyError:
            pass
