from typing import Tuple
from .Board import Board
from .pieces import Piece, Bishop, King, Knight, Pawn, Queen, Rook
from .Types import Color

_char_to_piece = {
    'B': Bishop,
    'K': King,
    'N': Knight,
    'P': Pawn,
    'Q': Queen,
    'R': Rook
}


class ParseException(Exception):
    """ Raised when the file is failed to parse """


class Parser:
    @staticmethod
    def _string_repr_to_piece_and_pos(string_repr: str, color: Color) -> Tuple[Piece, Tuple[str, int]]:
        return _char_to_piece[string_repr[0]](color), (string_repr[1], int(string_repr[2]))

    @staticmethod
    def parse_file(path: str) -> Tuple[Board, Board.BoardLocation]:
        b = Board()
        with open(path) as f:
            white_line = f.readline()
            if "WHITE: " == white_line[:7]:
                white_splits = [x.strip() for x in white_line[7:].split(",")]
            else:
                raise ParseException()
            black_line = f.readline()
            if "BLACK: " == black_line[:7]:
                black_splits = [x.strip() for x in black_line[7:].split(",")]
            else:
                raise ParseException()
            target_line = f.readline()
            if "PIECE TO MOVE: " == target_line[:15]:
                target_str = target_line[15:]
            else:
                raise ParseException()
        for str_representation in white_splits:
            piece, pos = Parser._string_repr_to_piece_and_pos(str_representation, Color.WHITE)
            b[pos] = piece
        for str_representation in black_splits:
            piece, pos = Parser._string_repr_to_piece_and_pos(str_representation, Color.BLACK)
            b[pos] = piece
        return b, b.get_board_location((target_str[1], int(target_str[2])))

    @staticmethod
    def parse_command_line():
        b = Board()
        white_splits = [x.strip() for x in input("WHITE: ").split(",")]
        black_splits = [x.strip() for x in input("BLACK: ").split(",")]
        target_str = input("PIECE TO MOVE: ").split(",")
        for str_representation in white_splits:
            piece, pos = Parser._string_repr_to_piece_and_pos(str_representation, Color.WHITE)
            b[pos] = piece
        for str_representation in black_splits:
            piece, pos = Parser._string_repr_to_piece_and_pos(str_representation, Color.BLACK)
            b[pos] = piece
        return b, b.get_board_location((target_str[1], int(target_str[2])))