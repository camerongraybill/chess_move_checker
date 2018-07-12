from typing import Optional, Tuple, Union
from .pieces.Piece import Piece
from copy import deepcopy

class Board:
    """ A representation of a board """

    class BoardLocation:
        def __init__(self, board, val: Optional[Piece] = None, location: Optional[Tuple[int, int]] = None):
            self._val: Optional[Piece] = val
            self._board = board
            if location is not None:
                self._x, self._y = location
            else:
                self._x = None
                self._y = None

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
        def empty(self):
            return self._val is None

        def __eq__(self, other):
            return self.__class__ == other.__class__ and self.value == other.value

    class Move:
        def __init__(self, initial_pos, final_pos):
            self._from = initial_pos
            self._to = final_pos

        @property
        def beg(self):
            return self._from

        @property
        def end(self):
            return self._to

        @property
        def traversed_pieces(self):
            start_pos = self._from.location
            end_pos = self._to.location
            board = self._from.board
            if start_pos[0] == end_pos[0]:
                # If the X values are the same then just iterate the Y
                for x in range(min(start_pos[1], end_pos[1]) + 1, max(start_pos[1], end_pos[1])):
                    yield board[start_pos[0], x]
            elif start_pos[1] == end_pos[1]:
                # If the Y values are the same then just iterate the X
                for x in range(min(start_pos[0], end_pos[0]) + 1, max(start_pos[0], end_pos[0])):
                    yield board[x, start_pos[1]]
            else:
                def get_increment_pair():
                    if start_pos[0] < end_pos[0]:
                        if start_pos[1] < end_pos[1]:
                            return 1, 1
                        else:
                            return 1, -1
                    else:
                        if start_pos[1] < end_pos[1]:
                            return -1, 1
                        else:
                            return -1, -1

                increment_value = get_increment_pair()
                x, y = start_pos
                x += increment_value[0]
                y += increment_value[1]
                while (x, y) != end_pos:
                    yield board[x, y]
                    x += increment_value[0]
                    y += increment_value[1]

    def __init__(self):
        self._state = {x: {y: Board.BoardLocation(board=self, location=(x + 1, y + 1)) for y in range(8)} for x in
                       range(8)}

    def apply_move_copy(self, move):
        cp = deepcopy(self)
        cp[move.end.location] = move.beg.value
        cp[move.beg.location] = None
        return cp

    def __getitem__(self, pair: Tuple[Union[str, int], int]):
        first, second = pair
        if isinstance(first, str):
            if len(first) != 1:
                raise TypeError()
            first = ord(first) - (ord("a") - 1)
        return self._state[first - 1][second - 1].value

    def __setitem__(self, pair: Tuple[Union[str, int], int], value: Optional[Piece]):
        first, second = pair
        if isinstance(first, str):
            if len(first) != 1:
                raise TypeError()
            first = ord(first) - (ord("a") - 1)
        self._state[first - 1][second - 1].value = value

    def get_board_location(self, pair: Tuple[Union[str, int], int]):
        first, second = pair
        if isinstance(first, str):
            if len(first) != 1:
                raise TypeError()
            first = ord(first) - (ord("a") - 1)
        return self._state[first - 1][second - 1]

    def __str__(self):
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
