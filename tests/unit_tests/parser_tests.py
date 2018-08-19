from unittest import TestCase
from chess_move_checker.Parser import Parser, ParseException
from chess_move_checker.Types import Color


class ParserTest(TestCase):

    def test_parse_exception(self):

        with self.assertRaises(ParseException):
            _ = Parser._string_repr_to_piece_and_pos("Zf3", Color.BLACK)
        with self.assertRaises(ParseException):
            _ = Parser._string_repr_to_piece_and_pos("K", Color.BLACK)
