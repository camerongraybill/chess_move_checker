from enum import Enum


class Color(Enum):
    BLACK = "black"
    WHITE = "white"

    @property
    def letter(self):
        return self.value[0]

    @property
    def direction(self):
        if self.value == "black":
            return -1
        else:
            return 1
