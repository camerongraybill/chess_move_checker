from .Types import Color
from .Board import Board
from .pieces import King, Bishop, Knight, Rook, Queen, Pawn
from collections import Counter
from .Utils import player_in_check, player_in_checkmate


class BoardStateValidator:
    class InvalidBoardStateException(Exception):
        """ Base class for when a board is invalid """

    class TooManyKings(InvalidBoardStateException):
        """ Raised when a color has too many kings """

    class TooManyPawns(InvalidBoardStateException):
        """ Raised when a color has too many pawns """

    class OpponentInCheck(InvalidBoardStateException):
        """ Raised when the opponent of the chosen piece is in check """

    class InCheckmate(InvalidBoardStateException):
        """ Raised when a player is in checkmate """

        def __init__(self, color: Color):
            self.color = color

    @staticmethod
    def validate(board: Board, next_color_to_go: Color):
        # Validate that:
        # Exactly 1 King of each color
        # No more than 8 Pawns/used to be pawns of each color
        # Neither player can be in checkmate
        # Opponent cannot be in check
        all_pieces = list(board.pieces())
        piece_counts = Counter(all_pieces)
        all_colors = (Color.BLACK, Color.WHITE)
        # Must be exactly one king of each color
        if piece_counts[King(Color.WHITE)] != 1 or piece_counts[King(Color.BLACK)] != 1:
            raise BoardStateValidator.TooManyKings()

        promotable_pieces = (Bishop, Knight, Rook)
        for color in all_colors:
            if sum(max(piece_counts[x(color)] - 2, 0) for x in promotable_pieces) \
                    + max(piece_counts[Queen(color)] - 1, 0) + piece_counts[Pawn(color)] > 8:
                raise BoardStateValidator.TooManyPawns()

        for color in all_colors:
            if player_in_checkmate(board, color):
                raise BoardStateValidator.InCheckmate(color)

        if player_in_check(board, next_color_to_go.opponent_color):
            raise BoardStateValidator.OpponentInCheck()
