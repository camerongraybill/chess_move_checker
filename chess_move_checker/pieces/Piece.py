from ..Types import Color
from abc import ABC, abstractmethod
from typing import List
from itertools import chain, product


class Piece(ABC):
    def __init__(self, color: Color):
        self._color = color

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.color == other.color

    @property
    def color(self):
        return self._color

    @property
    @abstractmethod
    def character(self):
        raise NotImplementedError()

    @abstractmethod
    def get_possible_moves(self, board, my_position) -> List:
        raise NotImplementedError()

    def get_valid_moves(self, board, my_position):
        for move in self.get_possible_moves(board, my_position):
            # Check if there is anything between start position and end position
            # And make sure that we are not moving into check
            if self._opponents_or_empty(move.end) and not any(move.traversed_pieces) and self._won_or_safe(move.applied_state):
                yield move

    @staticmethod
    def _is_color_in_check(board, color):
        for move in board.all_moves_for_color(color.opponent_color):
            if move.applied_state.is_winner(color.opponent_color):
                return True
        return False

    @staticmethod
    def _is_winner(board, color):
        return board.is_winner(color)

    @staticmethod
    def _get_incrementing_moves(board, start_position, increment):
        iter_position = start_position
        try:
            for _ in range(7):
                iter_position = board.get_board_location((
                    iter_position.location[0] + increment[0], iter_position.location[1] + increment[1]))
                yield board.Move(start_position, iter_position)
        except KeyError:
            pass

    @staticmethod
    def _get_diagonal_moves(board, position):
        for m in chain(Piece._get_incrementing_moves(board, position, (1, 1)),
                       Piece._get_incrementing_moves(board, position, (-1, -1)),
                       Piece._get_incrementing_moves(board, position, (-1, 1)),
                       Piece._get_incrementing_moves(board, position, (1, -1))):
            yield m

    @staticmethod
    def _get_hor_vert_moves(board, position):
        for m in chain(Piece._get_incrementing_moves(board, position, (1, 0)),
                       Piece._get_incrementing_moves(board, position, (0, 1)),
                       Piece._get_incrementing_moves(board, position, (-1, 0)),
                       Piece._get_incrementing_moves(board, position, (0, -1))):
            yield m

    @staticmethod
    def _get_one_move_away(board, position):
        x_pos = position.location[0]
        y_pos = position.location[1]

        for i, j in product(range(-1, 2), range(-1, 2)):
            try:
                if not (i, j) == (0, 0):
                    yield board.Move(position, board.get_board_location((x_pos + i, y_pos + j)))
            except KeyError:
                pass

    @staticmethod
    def _get_l_moves(board, position):
        x_pos = position.location[0]
        y_pos = position.location[1]

        for x, y in product([-2, -1, 1, 2], [-2, -1, 1, 2]):
            if abs(x) != abs(y):
                try:
                    yield board.Move(position, board.get_board_location((x_pos + x, y_pos + y)))
                except KeyError:
                    pass

    def _opponents_or_empty(self, board_position):
        return board_position.value is None or board_position.value.color == self.color.opponent_color

    def _won_or_safe(self, board):
        return self._player_won_or_safe(self.color, board)

    @staticmethod
    def _player_won_or_safe(color, board):
        return Piece._is_winner(board, color) or not Piece._is_color_in_check(board, color)
