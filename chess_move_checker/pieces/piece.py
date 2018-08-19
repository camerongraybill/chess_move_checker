from abc import ABC, abstractmethod
from typing import Generator

from ..types import Color
from ..utils import color_or_empty, player_in_check


class Piece(ABC):
    """ Represents and abstract piece, includes the logic for what moves are legal for this piece. """

    def __init__(self, color: Color):
        self._color = color

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__ and self.color == other.color

    def __hash__(self) -> int:
        return (self.character + self.color.value).__hash__()

    @property
    def color(self) -> Color:
        return self._color

    @property
    @abstractmethod
    def character(self) -> str:
        """ Get the character representation of this piece """
        raise NotImplementedError()

    @staticmethod
    def get_possible_moves(board, my_position) -> Generator:
        """ Get all moves in this piece's movement pattern """
        raise NotImplementedError()

    def get_valid_moves(self, board, my_position) -> Generator:
        """ Get all moves that are valid for this piece to make right now """
        for m in self.get_possible_moves(board, my_position):
            if self._validate_move(m):
                yield m

    def get_winning_moves(self, board, my_position) -> Generator:
        """ Get all moves that would win the game """
        for m in self.get_possible_moves(board, my_position):
            if m.is_winning_move and not any(m.traversed_pieces):
                yield m

    @staticmethod
    def _validate_move(move) -> bool:
        # For most pieces, a move is valid if:
        # The end location is an opponents piece or is empty
        # No Pieces are between the start and end
        # The player is not in check after the move
        return color_or_empty(move.end, move.piece.color.opponent_color) \
               and not any(move.traversed_pieces) \
               and not player_in_check(move.applied_state, move.piece.color)
