from typing import Sequence, Tuple

from commands import Command

class MenuState():
    def __init__(self, name: str, exits: Sequence[Tuple[Command, str]]):
        self.name = name
        self.exits = exits
