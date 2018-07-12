from .Board import Board
from typing import List


class MoveCalculator:
    def get_valid_moves(self, board: Board, position: Board.BoardLocation) -> List[Board.BoardLocation]:
        if position.empty:
            return []
        else:
            return position.value.get_possible_moves(board, position)

