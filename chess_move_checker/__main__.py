from argparse import ArgumentParser
from .Parser import Parser
from .MoveCalculator import MoveCalculator
from .BoardStateValidator import BoardStateValidator


def get_args():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input-file", type=str)
    return parser.parse_args()


def main():
    try:
        args = get_args()
        if args.input_file is not None:
            board, position = Parser.parse_file(args.input_file)
        else:
            board, position = Parser.parse_command_line()
        output_message = "LEGAL MOVES FOR {}{}{}:".format(position.value.character,
                                                          chr(ord('a') - 1 + position.location[0]), position.location[1])
        for move in MoveCalculator.get_valid_moves(board, position):
            output_message += " {}{},".format(chr(ord('a') - 1 + move.end.location[0]), move.end.location[1])
        print(output_message[:-1])
        BoardStateValidator.validate(board, position.value.color)
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
    from sys import exit as s_exit

    s_exit(main())
