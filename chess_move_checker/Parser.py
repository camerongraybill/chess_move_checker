from typing import Tuple

from .Board import Board
from .Types import Color
from .pieces import Piece, Bishop, King, Knight, Pawn, Queen, Rook

""" A Dictionary of letter to constructor for each of the pieces. """
_char_to_piece = {
    'B': Bishop,
    'K': King,
    'N': Knight,
    'P': Pawn,
    'Q': Queen,
    'R': Rook
}


class ParseException(Exception):
    """ Raised when the file failed to parse """


class Parser:
    """ Parses input to create a board and piece to move """
    @staticmethod
    def _string_repr_to_piece_and_pos(string_repr: str, color: Color) -> Tuple[Piece, Tuple[str, int]]:
        """ Turns a three character string and a color into a piece and it's location on the board. """
        try:
            return _char_to_piece[string_repr[0]](color), (string_repr[1], int(string_repr[2]))
        except KeyError:
            raise ParseException()
        except IndexError:
            raise ParseException()

    @staticmethod
    def parse_file(path: str) -> Tuple[Board, Board.BoardLocation]:
        """ Parse a file into a board and piece board location to get moves for"""
        b = Board()
        try:
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
            return b, b[target_str[1], int(target_str[2])]
        except KeyError:
            raise ParseException()
        except IndexError:
            raise ParseException()

    @staticmethod
    def parse_command_line():
        """ Prompt the user for input from command line """
        b = Board()
        white_splits = [x.strip() for x in input("WHITE: ").split(",")]
        black_splits = [x.strip() for x in input("BLACK: ").split(",")]
        target_str = input("PIECE TO MOVE: ").split(",")
        try:
            for str_representation in white_splits:
                piece, pos = Parser._string_repr_to_piece_and_pos(str_representation, Color.WHITE)
                b[pos] = piece
            for str_representation in black_splits:
                piece, pos = Parser._string_repr_to_piece_and_pos(str_representation, Color.BLACK)
                b[pos] = piece
            return b, b[target_str[1], int(target_str[2])]
        except KeyError:
            raise ParseException()
        except IndexError:
            raise ParseException()