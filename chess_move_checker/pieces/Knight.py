from .Piece import Piece
from ..Types import Color
from ..Utils import color_or_empty, player_in_check, MovementPatterns


class Knight(Piece):
    def __init__(self, color: Color):
        super(Knight, self).__init__(color)

    @property
    def character(self):
        return "N"

    @staticmethod
    def get_possible_moves(board, my_position):
        """ Knights move in an L """
        yield from MovementPatterns.get_l_moves(board, my_position)

    @staticmethod
    def _validate_move(move):
        # For Knight pieces, a move is valid if:
        # The end location is an opponents piece or is empty
        # The player is not in check after the move
        return color_or_empty(move.end, move.piece.color.opponent_color) \
               and not player_in_check(move.applied_state, move.piece.color)

    def get_winning_moves(self, board, my_position):
        """ Knights need to override the get winning moves function because they jump pieces """
        for m in self.get_possible_moves(board, my_position):
            if m.is_winning_move:
                yield m
