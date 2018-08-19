from .piece import Piece
from ..move import Move
from ..utils import player_in_check


class Pawn(Piece):
    @property
    def character(self):
        return "P"

    @staticmethod
    def get_possible_moves(board, my_position):
        """ Pawns can either move forward one square,
        forward two squares if on home row, or attack to a forward diagonal """
        for x in (-1, 0, 1):
            try:
                yield Move(my_position, board[my_position.x + x, my_position.y + my_position.value.color.direction])
            except KeyError:
                pass
        # Try to double move if on home row
        if my_position.y == my_position.value.color.home_row:
            yield Move(my_position, board[my_position.x, my_position.y + 2 * my_position.value.color.direction])

    @staticmethod
    def _validate_move(move):
        """ Pawns move validity is different because it can only attack on angles and only move on straight """
        if move.beg.x == move.end.x:
            # Moving forward, no x change
            # There must not be a piece there and can't move into check
            return move.end.empty and not player_in_check(move.applied_state, move.piece.color) and not any(
                move.traversed_pieces)
        else:
            # Diagonal move, must be attack
            # Must have opponents piece and can't move into check
            return (not move.end.empty and move.end.value.color == move.piece.color.opponent_color) \
                   and not player_in_check(move.applied_state, move.piece.color)

    def get_winning_moves(self, board, my_position):
        """ A pawn can't actually ever get any winning moves, but theoretically it could.
        Validate that it is an attack. """
        for m in self.get_possible_moves(board, my_position):
            if m.is_winning_move and m.beg.x != m.end.x:
                yield m
