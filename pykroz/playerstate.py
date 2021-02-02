from typing import Optional, Tuple
from pieces import What, WhatSets

class PlayerState():
    def __init__(self):
        self.score: int = 0
        self.whip_power: int = 0
        self.level: int = 0
        self.gems: int = 0
        self.whips: int = 0
        self.teleports: int = 0
        self.keys: int = 0

        self.position: Tuple[int, int] = (0, 0)

        self.invisibility_remaining: float = 0

    def future_pos(self, x_offset: int, y_offset: int) -> Tuple[int, int]:
        (x, y) = self.position
        return (x + x_offset, y + y_offset)

    def add_score(self, score: int):
        if score > 0 or self.score + score > 0:
            self.score += score
