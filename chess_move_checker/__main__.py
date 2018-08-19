from argparse import ArgumentParser, Namespace

from .board_state_validator import BoardStateValidator
from .parser import Parser, ParseException


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
        valid_moves = list(position_to_check.value.get_valid_moves(board, position_to_check))
        # Format everything to print
        string_of_location_to_check = position_to_check.value.character + chr(ord('a') - 1 + position_to_check.x) + str(
            position_to_check.y)
        if valid_moves:
            output_message = "LEGAL MOVES FOR {}:".format(string_of_location_to_check)
            for move in valid_moves:
                output_message += " {}{},".format(chr(ord('a') - 1 + move.end.x), move.end.y)
            output_message = output_message[:-1]
        else:
            output_message = "NO LEGAL MOVES FOR {}".format(string_of_location_to_check)
        print(output_message)
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


if __name__ == '__main__':
    # If run from the command line, call main() and exit with it's return code
    from sys import exit as s_exit

    s_exit(main())
