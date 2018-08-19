from copy import deepcopy
from itertools import chain
from typing import Optional, Tuple, Union

from .Types import Color
from .pieces import Piece, King, Pawn, Queen, Bishop, Rook, Knight


class Board:
    """ A representation of a board """

    class BoardLocation:
        """ Represents a square on the board """
        def __init__(self, board, val: Optional[Piece] = None, location: Optional[Tuple[int, int]] = None):
            self._val: Optional[Piece] = val
            self._board = board
            self._x, self._y = location

        def debug_string(self):
            return "({x},{y}): {item}".format(x=self._x, y=self._y, item=self._val)

        @property
        def board(self):
            return self._board

        def __str__(self):
            if isinstance(self._val, Piece):
                return self._val.color.letter + self._val.character
            else:
                return "  "

        def __repr__(self):
            return self.__str__()

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

        def __eq__(self, other):
            return self.__class__ == other.__class__ and self.value == other.value

    def __init__(self):
        """ Initialize a board to 8x8 empty spaces """
        self._state = {x: {y: Board.BoardLocation(board=self, location=(x + 1, y + 1)) for y in range(8)} for x in
                       range(8)}

    @staticmethod
    def get_default_board():
        """ Get a Board that would represent the start of a game """
        b = Board()
        for i in range(8):
            b[i + 1, 2] = Pawn(Color.WHITE)
            b[i + 1, 7] = Pawn(Color.BLACK)
        for i in ('a', 'h'):
            b[i, 1] = Rook(Color.WHITE)
            b[i, 8] = Rook(Color.BLACK)
        for i in ('b', 'g'):
            b[i, 1] = Knight(Color.WHITE)
            b[i, 8] = Knight(Color.BLACK)
        for i in ('c', 'f'):
            b[i, 1] = Bishop(Color.WHITE)
            b[i, 8] = Bishop(Color.BLACK)
        b['d', 1] = Queen(Color.WHITE)
        b['d', 8] = Queen(Color.BLACK)
        b['e', 1] = King(Color.WHITE)
        b['e', 8] = King(Color.BLACK)
        return b

    def apply_move_copy(self, move):
        """ Apply a move to a copy of the current board, then return that board. """
        cp = deepcopy(self)
        cp[move.end.location] = move.beg.value
        cp[move.beg.location] = None
        return cp

    def __getitem__(self, pair: Tuple[Union[str, int], int]) -> BoardLocation:
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

    def __str__(self):
        """ String representation of a board """
        bar = "|-----------------------|"
        out = " ----------------------- "
        for i in range(7, -1, -1):
            out += "\n"
            for j in range(8):
                out += "|"
                out += str(self._state[j][i])
            out += "|"
            out += "\n"
            if i != 0:
                out += bar
        out += " ----------------------- "
        return out

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        for y in self._state.values():
            yield from y.values()

    def pieces(self):
        """ Get all of the pieces on the board """
        for x in self:
            if not x.empty:
                yield x.value

    @property
    def winner(self):
        # Assume that this is at most one move after a valid board state so there should be at least 1 king
        pieces_of_board = list(self.pieces())
        black_king_exists = King(Color.BLACK) in pieces_of_board
        white_king_exists = King(Color.WHITE) in pieces_of_board
        if black_king_exists and white_king_exists:
            return None
        elif black_king_exists:
            return Color.WHITE
        else:
            return Color.BLACK
