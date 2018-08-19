from argparse import ArgumentParser, Namespace
from random import choice
from time import sleep

from .Board import Board
from .BoardStateValidator import BoardStateValidator
from .Parser import Parser, ParseException
from .Types import Color
from .Utils import get_valid_moves_for


def get_args() -> Namespace:
    """ Parse the command line arguments for the program """
    parser = ArgumentParser()
    parser.add_argument("-i", "--input-file", type=str)
    return parser.parse_args()


def main() -> int:
    """ Main entry point to the program:
        will parse the input
        validate the board
        and then calculate the valid moves """
    try:
        # Get command line args to check if the user game a board file
        args = get_args()
        # Load a board and position to check
        if args.input_file is not None:
            board, position_to_check = Parser.parse_file(args.input_file)
        else:
            board, position_to_check = Parser.parse_command_line()
        # Validate that the board is in a valid state
        BoardStateValidator.validate(board, position_to_check.value.color)
        # Get all of the valid moves
        valid_moves = position_to_check.value.get_valid_moves(board, position_to_check)
        # Format everything to print
        string_of_location_to_check = position_to_check.value.character + chr(ord('a') - 1 + position_to_check.x) + str(
            position_to_check.y)

        output_message = "LEGAL MOVES FOR {}:".format(string_of_location_to_check)
        for move in valid_moves:
            output_message += " {}{},".format(chr(ord('a') - 1 + move.end.x), move.end.y)
        print(output_message[:-1])
        return 0
    except ParseException:
        print("Failed to parse input")
        return 1
    except BoardStateValidator.InCheckmate as ex:
        print("Invalid board state: {color} is in checkmate".format(color=ex.color.value))
        return 1
    except BoardStateValidator.OpponentInCheck:
        print("Invalid board state: Opponent cannot be in check")
        return 1
    except BoardStateValidator.TooManyKings:
        print("Invalid board state: Each player must have exactly one king")
        return 1
    except BoardStateValidator.TooManyPawns:
        print("Invalid board state: Each player cannot have more than 8 pawns or promoted pieces")
        return 1


def play_game():
    current_player = Color.WHITE
    current_board = Board.get_default_board()
    print(current_board)
    while not current_board.winner:
        print(current_board)
        move = choice(list(get_valid_moves_for(current_board, current_player)))
        print(move.beg, move.end)
        current_board = current_board.apply_move_copy(move)
        current_player = current_player.opponent_color
        sleep(.5)


def visualize_board(path_to_board):
    board, position = Parser.parse_file(path_to_board)
    print(board)
    print(position)


if __name__ == '__main__':
    """ If run from the command line, call main() and exit with it's return code """
    from sys import exit as s_exit

    s_exit(main())
