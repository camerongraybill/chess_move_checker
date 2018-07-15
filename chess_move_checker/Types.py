from enum import Enum


class Color(Enum):
    BLACK = "black"
    WHITE = "white"

    @property
    def letter(self):
        # pylint: disable=unsubscriptable-object
        return self.value[0]

    @property
    def direction(self):
        if self == Color.BLACK:
            return -1
        else:
            return 1

    @property
    def opponent_color(self):
        if self == Color.BLACK:
            return Color.WHITE
        else:
            return Color.BLACK
