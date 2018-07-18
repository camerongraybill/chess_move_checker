from argparse import ArgumentParser
from .Parser import Parser
from .MoveCalculator import MoveCalculator
from .BoardStateValidator import BoardStateValidator
from .Types import Color
from .Board import Board
from .Utils import get_valid_moves_for
from random import choice
from time import sleep


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
        BoardStateValidator.validate(board, position.value.color)
        output_message = "LEGAL MOVES FOR {}{}{}:".format(position.value.character,
                                                          chr(ord('a') - 1 + position.location[0]),
                                                          position.location[1])
        for move in MoveCalculator.get_valid_moves(board, position):
            output_message += " {}{},".format(chr(ord('a') - 1 + move.end.location[0]), move.end.location[1])
        print(output_message[:-1])
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


if __name__ == '__main__':
    from sys import exit as s_exit

    s_exit(main())
