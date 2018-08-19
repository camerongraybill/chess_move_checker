from copy import deepcopy
from typing import Optional, Tuple, Union

from .pieces import Piece


class Board:
    """ A representation of a board """

    class BoardLocation:
        """ Represents a square on the board """

        def __init__(self, board, val: Optional[Piece] = None, location: Optional[Tuple[int, int]] = None):
            self._val: Optional[Piece] = val
            self._board = board
            self._x, self._y = location

        @property
        def board(self):
            return self._board

        @property
        def value(self):
            return self._val

        @value.setter
        def value(self, value: Optional[Piece]):
            self._val = value

        @property
        def location(self):
            return self._x, self._y

        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y

        @property
        def empty(self):
            return self._val is None

    def __init__(self):
        """ Initialize a board to 8x8 empty spaces """
        self._state = {x: {y: Board.BoardLocation(board=self, location=(x + 1, y + 1)) for y in range(8)} for x in
                       range(8)}

    def apply_move_copy(self, move):
        """ Apply a move to a copy of the current board, then return that board. """
        cp = deepcopy(self)
        cp[move.end.location] = move.beg.value
        cp[move.beg.location] = None
        return cp

    def __getitem__(self, pair: Tuple[Union[str, int], int]):
        """ Get a value from a location on the board """
        first, second = pair
        if isinstance(first, str):
            if len(first) != 1:
                raise TypeError()
            first = ord(first) - (ord("a") - 1)
        return self._state[first - 1][second - 1]

    def __setitem__(self, pair: Tuple[Union[str, int], int], value: Optional[Piece]):
        """ Set a value into the board """
        first, second = pair
        if isinstance(first, str):
            if len(first) != 1:
                raise TypeError()
            first = ord(first) - (ord("a") - 1)
        self._state[first - 1][second - 1].value = value

    def __iter__(self):
        for y in self._state.values():
            yield from y.values()

    def pieces(self):
        """ Get all of the pieces on the board """
        for x in self:
            if not x.empty:
                yield x.value
