class Move:
    """ Represents a move from one position to another """

    def __init__(self, initial_pos, final_pos):
        self._from = initial_pos
        self._to = final_pos

    @property
    def piece(self):
        return self._from.value

    @property
    def beg(self):
        return self._from

    @property
    def end(self):
        return self._to

    @property
    def applied_state(self):
        """ Get what the board would look like after applying this move """
        return self.end.board.apply_move_copy(self)

    @property
    def is_winning_move(self):
        """ Check if this move would win the game """
        return not self.end.empty \
               and self.end.value.color == self.piece.color.opponent_color \
               and self.end.value.character == "K"

    @property
    def traversed_pieces(self):
        """ Get the list of all pieces between the move's begin and end pieces """
        if self._from.x == self._to.x:
            # If the X values are the same then just iterate the Y
            for y in range(min(self._from.y, self._to.y) + 1, max(self._from.y, self._to.y)):
                yield self._from.board[self._from.x, y].value
        elif self._from.y == self._to.y:
            # If the Y values are the same then just iterate the X
            for x in range(min(self._from.x, self._to.x) + 1, max(self._from.x, self._to.x)):
                yield self._from.board[x, self._from.y].value
        else:
            # Otherwise, iterate along the diagonal
            if self._from.x < self._to.x:
                if self._from.y < self._to.y:
                    increment_value = 1, 1
                else:
                    increment_value = 1, -1
            else:
                if self._from.y < self._to.y:
                    increment_value = -1, 1
                else:
                    increment_value = -1, -1

            x, y = self._from.x, self._from.y
            x += increment_value[0]
            y += increment_value[1]
            while (x, y) != self._to.location:
                yield self._from.board[x, y].value
                x += increment_value[0]
                y += increment_value[1]
