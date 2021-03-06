from enum import Enum
from random import choice, randrange
from typing import Sequence
from pygame import Color

class Colors:
    Black = Color("#000000")
    Blue = Color("#0000aa")
    Green = Color("#00aa00")
    Cyan = Color("#00aaaa")
    Red = Color("#aa0000")
    Magenta = Color("#aa00aa")
    Brown = Color("#aa5500")
    LightGrey = Color("#aaaaaa")
    DarkGrey = Color("#555555")
    LightBlue = Color("#5555ff")
    LightGreen = Color("#55ff55")
    LightCyan = Color("#55ffff")
    LightRed = Color("#ff5555")
    LightMagenta = Color("#ff55ff")
    Yellow = Color("#ffff55")
    White = Color("#ffffff")

    @staticmethod
    def Random() -> Color:
        return choice([
            Colors.Black, Colors.Blue, Colors.Green, Colors.Cyan, Colors.Red, Colors.Magenta, Colors.Brown, Colors.DarkGrey,
            Colors.LightGrey, Colors.LightBlue, Colors.LightGreen, Colors.LightCyan, Colors.LightRed, Colors.LightMagenta, Colors.Yellow, Colors.White
        ])

    @staticmethod
    def RandomDark() -> Color:
        return choice([
            Colors.Black, Colors.Blue, Colors.Green, Colors.Cyan, Colors.Red, Colors.Magenta, Colors.Brown, Colors.DarkGrey
        ])

    @staticmethod
    def RandomLight() -> Color:
        return choice([
            Colors.LightGrey, Colors.LightBlue, Colors.LightGreen, Colors.LightCyan, Colors.LightRed, Colors.LightMagenta, Colors.Yellow, Colors.White
        ])

    @staticmethod
    def RandomExcept(exclude: Sequence[Color]) -> Color:
        cols = set(Colors.Code.values())
        return choice(cols.difference(exclude))

    Code = {
        0: Black,
        1: Blue,
        2: Green,
        3: Cyan,
        4: Red,
        5: Magenta,
        6: Brown,
        7: LightGrey,
        8: DarkGrey,
        9: LightBlue,
        10: LightGreen,
        11: LightCyan,
        12: LightRed,
        13: LightMagenta,
        14: Yellow,
        15: White
    }


class ContrastLevel(Enum):
    DARKEST = 1
    DARKER = 2
    LIGHTER = 3
    LIGHTEST = 4

    @staticmethod
    def Random():
        return ContrastLevel(randrange(len(ContrastLevel)) + 1)
