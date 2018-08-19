from enum import Enum


class Color(Enum):
    """ Represents the color of a player, defines some constants that are different depending on the color """
    BLACK = "black"
    WHITE = "white"

    @property
    def direction(self):
        """ The direction a player's pieces can move """
        if self == Color.BLACK:
            return -1
        else:
            return 1

    @property
    def home_row(self):
        """ The location of a player's home row (starting pawn row) """
        if self == Color.BLACK:
            return 7
        else:
            return 2

    @property
    def opponent_color(self):
        if self == Color.BLACK:
            return Color.WHITE
        else:
            return Color.BLACK
