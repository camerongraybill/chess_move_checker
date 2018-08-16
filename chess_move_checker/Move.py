class Move:
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
        return self.end.board.apply_move_copy(self)

    @property
    def is_winning_move(self):
        # Check if this move takes the opponent's king
        return not self.end.empty\
               and self.end.value.color == self.piece.color.opponent_color\
               and self.end.value.character == "K"

    @property
    def traversed_pieces(self):
        start_pos = self._from.location
        end_pos = self._to.location
        board = self._from.board
        if start_pos[0] == end_pos[0]:
            # If the X values are the same then just iterate the Y
            for x in range(min(start_pos[1], end_pos[1]) + 1, max(start_pos[1], end_pos[1])):
                yield board[start_pos[0], x].value
        elif start_pos[1] == end_pos[1]:
            # If the Y values are the same then just iterate the X
            for x in range(min(start_pos[0], end_pos[0]) + 1, max(start_pos[0], end_pos[0])):
                yield board[x, start_pos[1]].value
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
                yield board[x, y].value
                x += increment_value[0]
                y += increment_value[1]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{},{} -> {},{}".format(self.beg.x, self.beg.y, self.end.x, self.end.y)
