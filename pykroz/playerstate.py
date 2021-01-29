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

        self.position: Optional[Tuple[int, int]] = (0, 0)

        self.invisibility_remaining: float = 0

    def future_pos(self, x_offset: int, y_offset: int) -> Tuple[int, int]:
        (x, y) = self.position
        return (x + x_offset, y + y_offset)

    def add_score(self, what: What):
        if what in WhatSets.monsters: # Monsters
            self.score += int(What)
        elif what in (What.Breakable_Wall, What.Wall): # Block
            if self.score > 2:
                self.score -= 2
        elif what == 5: # Whip
            self.score += 1
        elif what == 6: # Stairs
            self.score += self.level
        elif what == 7: # Chest
            self.score += 5
        elif what == 9: # Gem
            self.score += 1
        elif what == 10: # Invisible
            self.score += 10
        elif what == 11: # Teleport
            self.score += 1
        elif what == 15: # SpeedTime
            self.score += 2
        elif what == 16: # Trap
            if self.score > 5:
                self.score -= 5
        elif what == 22: # Lava
            self.score += 25
        elif what == 20: # Border
            if self.score > self.level:
                self.score -= self.level // 2
        elif what == 27: # Nugget
            self.score += 50
        elif what == 35: # Create
            self.score += self.level * 2
        elif what == 36: # Generator
            self.score += 50
        elif what == 38: # MBlock
            self.score += 1
