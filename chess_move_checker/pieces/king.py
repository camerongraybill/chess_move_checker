from .piece import Piece
from ..utils import MovementPatterns


class King(Piece):
    @property
    def character(self):
        return "K"

    @staticmethod
    def get_possible_moves(board, my_position):
        """ Kings can move one spot away in any direction """
        yield from MovementPatterns.get_one_move_away(board, my_position)
