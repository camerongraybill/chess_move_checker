from ..Types import Color
from abc import ABC, abstractmethod
from typing import List
from ..Utils import color_or_empty, player_in_check


class Piece(ABC):
    def __init__(self, color: Color):
        self._color = color

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.color == other.color

    def __hash__(self):
        return (self.character + self.color.value).__hash__()

    @property
    def color(self):
        return self._color

    @property
    @abstractmethod
    def character(self):
        raise NotImplementedError()

    @staticmethod
    def get_possible_moves(board, my_position) -> List:
        raise NotImplementedError()

    def get_valid_moves(self, board, my_position):
        return (m for m in self.get_possible_moves(board, my_position) if self._validate_move(m))

    def get_winning_moves(self, board, my_position):
        return (m for m in self.get_possible_moves(board, my_position) if m.is_winning_move
                and not any(m.traversed_pieces))

    @staticmethod
    def _validate_move(move):
        # For most pieces, a move is valid if:
        # The end location is an opponents piece or is empty
        # No Pieces are between the start and end
        # The player is not in check after the move
        return color_or_empty(move.end, move.piece.color.opponent_color) \
               and not any(move.traversed_pieces) \
               and not player_in_check(move.applied_state, move.piece.color)
