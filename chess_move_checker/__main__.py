from argparse import ArgumentParser
from .Parser import Parser
from .MoveCalculator import MoveCalculator


def get_args():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input-file", type=str, required=True)
    return parser.parse_args()


def main():
    args = get_args()
    board, position = Parser.parse_file(args.input_file)
    output_message = "LEGAL MOVES FOR {}{}{}:".format(position.value.character, chr(ord('a') - 1 + position.location[0]), position.location[1])
    for move in MoveCalculator.get_valid_moves(board, position):
        output_message += " {}{},".format(chr(ord('a') - 1 + move.end.location[0]), move.end.location[1])
    print(output_message[:-1])


if __name__ == '__main__':
    from sys import exit as s_exit

    s_exit(main())
