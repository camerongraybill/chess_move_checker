from .Piece import Piece
from ..Types import Color
from ..Utils import MovementPatterns


class King(Piece):
    def __init__(self, color: Color):
        super(King, self).__init__(color)

    @property
    def character(self):
        return "K"

    @staticmethod
    def get_possible_moves(board, my_position):
        """ Kings can move one spot away in any direction """
        yield from MovementPatterns.get_one_move_away(board, my_position)
