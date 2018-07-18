from itertools import chain, product
from .Move import Move
from typing import Tuple


class MovementPatterns:
    @staticmethod
    def _get_incrementing_moves(board, start_position, increment: Tuple[int, int]):
        iter_position = start_position
        x_incr, y_incr = increment
        try:
            for _ in range(7):
                iter_position = board[iter_position.x + x_incr, iter_position.y + y_incr]
                yield Move(start_position, iter_position)
        except KeyError:
            pass

    @staticmethod
    def get_diagonal_moves(board, position):
        for m in chain.from_iterable(
                MovementPatterns._get_incrementing_moves(board, position, direction) for direction in
                product((1, -1), repeat=2)):
            yield m

    @staticmethod
    def get_hor_vert_moves(board, position):
        for m in chain.from_iterable(
                MovementPatterns._get_incrementing_moves(board, position, direction) for direction in
                ((1, 0), (0, 1), (-1, 0), (0, -1))):
            yield m

    @staticmethod
    def get_one_move_away(board, position):
        for x, y in product(range(-1, 2), repeat=2):
            try:
                if not (x, y) == (0, 0):
                    yield Move(position, board[position.x + x, position.y + y])
            except KeyError:
                pass

    @staticmethod
    def get_l_moves(board, position):
        for x, y in product([-2, -1, 1, 2], repeat=2):
            if abs(x) != abs(y):
                try:
                    yield Move(position, board[position.x + x, position.y + y])
                except KeyError:
                    pass


def get_moves_for(board, color):
    for position in board:
        if not position.empty and position.value.color == color:
            for x in position.value.get_possible_moves(board, position):
                yield x


def get_winning_moves_for(board, color):
    for position in board:
        if not position.empty and position.value.color == color:
            for x in position.value.get_winning_moves(board, position):
                yield x


def get_valid_moves_for(board, color):
    for position in board:
        if not position.empty and position.value.color == color:
            for x in position.value.get_valid_moves(board, position):
                yield x


def color_or_empty(board_location, color):
    return board_location.empty or board_location.value.color == color


def player_in_check(board, color):
    # A player is in check if any of their opponent's moves can take their king
    return any(get_winning_moves_for(board, color.opponent_color))


def player_in_checkmate(board, color):
    # A player is in checkmate if they can't make any moves
    return len(list(get_valid_moves_for(board, color))) == 0
