from os import path
from unittest import TestCase
from unittest.mock import patch

from chess_move_checker.parser import Parser, ParseException
from chess_move_checker.types import Color


class MockInputCall:
    def __init__(self, items):
        self._my_iterator = iter(items)

    def __call__(self, *args, **kwargs):
        return next(self._my_iterator)


class ParserTest(TestCase):

    def test_parse_exception(self):
        with self.assertRaises(ParseException):
            _ = Parser._string_repr_to_piece_and_pos("Zf3", Color.BLACK)
        with self.assertRaises(ParseException):
            _ = Parser._string_repr_to_piece_and_pos("K", Color.BLACK)

    @patch("chess_move_checker.parser.input",
           MockInputCall(("Rf1, Kg1, Pf2, Ph2, Pg3", "Kb8, Ne8, Pa7, Pb7, Pc7, Ra5", "Rf1")))
    def test_parse_command_line(self):
        """ Validate that the parse command line function works and produces the same results as parsing a file"""
        cmd_board, cmd_piece = Parser.parse_command_line()
        file_board, file_piece = Parser.parse_file(
            path.join(path.dirname(path.abspath(__file__)), "..", "regression_tests", "inputs", "1.input.txt"))
        for pair in zip(cmd_board.pieces(), file_board.pieces()):
            self.assertEqual(pair[0], pair[1])
        self.assertEqual(cmd_piece.value, file_piece.value)
