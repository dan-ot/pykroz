from collections.abc import Iterable
from playerstate import PlayerState
from typing import MutableMapping, Tuple, Union
from random import choice

from pygame import Rect

from pieces import What, parse
from levels import LiteralLevel, RandomLevel


class Playfield(MutableMapping[Tuple[int, int], What]):
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__data = [What.Nothing for _ in range(width * height)]
        self.replacement = What.Nothing

    def __len__(self) -> int:
        return len(self.__data)

    def __getitem__(self, key: Tuple[int, int]) -> What:
        if len(key) != 2:
            raise KeyError("Expected key of length 2 (x, y) but got: {0}".format(key))
        x, y = key
        if x >= self.__width or y >= self.__height:
            raise KeyError("{0} is out of bounds ({1}, {2} max)".format(key, self.__width, self.__height))

        return self.__data[x * self.__width + y]

    def __setitem__(self, key: Tuple[int, int], value: Union[What]) -> None:
        if len(key) != 2:
            raise KeyError("Expected key of length 2 (x, y) but got: {0}".format(key))
        x, y = key
        if x >= self.__width or y >= self.__height:
            raise KeyError("{0} is out of bounds({1}, {2} max)".format(key, self.__width, self.__height))

        self.__data[x * self.__width + y] = What(value)

    def __delitem__(self, v: Tuple[int, int]) -> None:
        self.__setitem__(v, What.Nothing)

    def __iter__(self):
        return iter(self.__data)

    def bounds(self) -> Rect:
        return Rect(0, 0, self.__width, self.__height)

    def count_of(self, what: What) -> int:
        return self.__data.count(what)

    def coords_of(self, what_set: Union[Iterable[What], What]) -> list[Tuple[int, int, What]]:
        if not isinstance(what_set, Iterable) and not isinstance(what_set, What):
            raise TypeError("Expected an Iterable of What or a What directly: {0}".format(what_set))
        check = what_set if isinstance(what_set, Iterable) else [what_set]
        return [(
            index // self.__width,
            index % self.__width,
            value) for (index, value)
                in enumerate(self.__data)
                if value in check]

    def reset(self, base: What = What.Nothing) -> None:
        self.__data = [base for _ in range(self.__width * self.__height)]

    def parse(self, level: LiteralLevel) -> None:
        if len(level.lines) != self.__height:
            raise ValueError("Expected {0} lines, got {1}".format(self.__height, len(level.lines)))

        for y, line in enumerate(level.lines):
            if len(line) != self.__width:
                raise ValueError("Line {0} length was {1}, expected {2}".format(y, len(line), self.__width))
            for x, char in enumerate(line):
                what = parse(char)
                self[x, y] = what

    def generate(self, level: RandomLevel) -> None:
        for (what, count) in level.what_counts:
            for _ in range(count):
                empties = self.coords_of(What.Nothing)
                (x, y, _) = choice(empties)
                self[x, y] = what

    @staticmethod
    def from_level_definition(level: Union[LiteralLevel, RandomLevel], player: PlayerState) -> 'Playfield':
        if isinstance(level, RandomLevel):
            pf = Playfield(level.width, level.height)
            pf[player.position] = What.Player
            for (what, count) in level.what_counts:
                for _ in range(count):
                    empties = pf.coords_of(What.Nothing)
                    (x, y, _) = choice(empties)
                    pf[x, y] = what
        else:
            pf = Playfield(len(level.lines[0]), len(level.lines))
            for y, line in enumerate(level.lines):
                if len(line) != pf.__width:
                    raise ValueError(f"Line {y} length was {len(line)}, expected {pf.__width}")
                for x, char in enumerate(line):
                    what = parse(char)
                    pf[x, y] = what
        return pf
