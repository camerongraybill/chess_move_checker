from .Board import Board
from .Move import Move
from typing import List


class MoveCalculator:
    @staticmethod
    def get_valid_moves(board: Board, position: Board.BoardLocation) -> List[Move]:
        if position.empty:
            return []
        else:
            return list(position.value.get_valid_moves(board, position))
