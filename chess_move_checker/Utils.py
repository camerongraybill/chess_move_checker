from itertools import product
from typing import Tuple, Generator

from .move import Move


class MovementPatterns:
    """ All of the movement patterns for the pieces """

    @staticmethod
    def _get_incrementing_moves(board, start_position, increment: Tuple[int, int]) -> Generator[Move, None, None]:
        """ Get moves based on a starting position and a increment to repeatedly apply until it gets off the board. """
        iter_position = start_position
        x_incr, y_incr = increment
        try:
            for _ in range(7):
                iter_position = board[iter_position.x + x_incr, iter_position.y + y_incr]
                yield Move(start_position, iter_position)
        except KeyError:
            return

    @staticmethod
    def get_diagonal_moves(board, position) -> Generator[Move, None, None]:
        """ Get all diagonal moves from a location. """
        for direction in product((1, -1), repeat=2):
            yield from MovementPatterns._get_incrementing_moves(board, position, direction)

    @staticmethod
    def get_hor_vert_moves(board, position) -> Generator[Move, None, None]:
        """ Get all horizontal and vertical moves from a position """
        for direction in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            yield from MovementPatterns._get_incrementing_moves(board, position, direction)

    @staticmethod
    def get_one_move_away(board, position) -> Generator[Move, None, None]:
        """ Get all moves that are one space away"""
        for x, y in product(range(-1, 2), repeat=2):
            try:
                if (x, y) != (0, 0):
                    yield Move(position, board[position.x + x, position.y + y])
            except KeyError:
                pass

    @staticmethod
    def get_l_moves(board, position) -> Generator[Move, None, None]:
        """ Get all moves that are in an L shape """
        for x, y in product([-2, -1, 1, 2], repeat=2):
            if abs(x) != abs(y):
                try:
                    yield Move(position, board[position.x + x, position.y + y])
                except KeyError:
                    pass


def get_winning_moves_for(board, color) -> Generator[Move, None, None]:
    """ Get all the winning moves for a color """
    for position in board:
        if not position.empty and position.value.color == color:
            yield from position.value.get_winning_moves(board, position)


def get_valid_moves_for(board, color) -> Generator[Move, None, None]:
    """ Get all the valid moves for a color """
    for position in board:
        if not position.empty and position.value.color == color:
            yield from position.value.get_valid_moves(board, position)


def color_or_empty(board_location, color) -> bool:
    """ Check if a board location is either empty or is the given color """
    return board_location.empty or board_location.value.color == color


def player_in_check(board, color) -> bool:
    """ Check if the player is in check """
    # A player is in check if any of their opponent's moves can take their king
    return any(get_winning_moves_for(board, color.opponent_color))


def player_in_checkmate(board, color) -> bool:
    """ Check if the player is in checkmate """
    # A player is in checkmate if they can't make any moves
    return len(list(get_valid_moves_for(board, color))) == 0
