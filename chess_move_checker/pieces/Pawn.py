from .Piece import Piece
from ..Types import Color
from ..Utils import player_in_check
from ..Move import Move


class Pawn(Piece):
    def __init__(self, color: Color):
        super(Pawn, self).__init__(color)

    @property
    def character(self):
        return "P"

    @staticmethod
    def get_possible_moves(board, my_position):
        y_position = my_position.y + my_position.value.color.direction
        for x in (-1, 0, 1):
            try:
                yield Move(my_position, board[my_position.x + x, y_position])
            except KeyError:
                pass
        try:
            if my_position.y == my_position.value.color.home_row:
                yield Move(my_position, board[my_position.x, my_position.y + 2 * my_position.value.color.direction])
        except KeyError:
            pass

    @staticmethod
    def _validate_move(move):
        if move.beg.x == move.end.x:
            # Moving forward, no x change
            # There must not be a piece there and can't move into check
            return move.end.empty and not player_in_check(move.applied_state, move.piece.color) and not any(move.traversed_pieces)
        else:
            # Diagonal move, must be attack
            # Must have opponents piece and can't move into check
            return (not move.end.empty and move.end.value.color == move.piece.color.opponent_color) \
                   and not player_in_check(move.applied_state, move.piece.color)

    def get_winning_moves(self, board, my_position):
        return (m for m in self.get_possible_moves(board, my_position) if m.is_winning_move
                and m.beg.x != m.end.x)
