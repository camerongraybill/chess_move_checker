from ..Types import Color
from abc import ABC, abstractmethod
from typing import List
from itertools import chain, product


class Piece(ABC):
    def __init__(self, color: Color):
        self._color = color

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

    def _am_i_in_check(self, board):
        return False

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

    def _get_l_moves(self, board, position):
        x_pos = position.location[0]
        y_pos = position.location[1]

        for x, y in product([-2, -1, 1, 2], [-2, -1, 1, 2]):
            if abs(x) != abs(y):
                try:
                    yield board.Move(position, board((x_pos + x, y_pos + y)))
                except KeyError:
                    pass
