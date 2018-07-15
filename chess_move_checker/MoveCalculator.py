from .Board import Board
from typing import List


class MoveCalculator:
    @staticmethod
    def get_valid_moves(board: Board, position: Board.BoardLocation) -> List[Board.BoardLocation]:
        if position.empty:
            return []
        else:
            return position.value.get_valid_moves(board, position)

