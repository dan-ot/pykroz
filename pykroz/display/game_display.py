from enum import Enum
from typing import Optional, Tuple
from random import choice, randrange

from pygame import Color, Rect

from engine.colors import Colors
from engine.crt import Crt
from levels import VisibilityFlags
from pieces import VisibleTiles, What, chance_of, draw
from playerstate import PlayerState
from playfield import Playfield


class GameDisplay():
    BLINK_RATE = 300.0
    COLOR_RATE = 60.0

    def __init__(self, playfield_rect: Rect):
        self.mpf = MainPlayfield(playfield_rect, Colors.Black, VisibilityFlags.SHOW_ALL)
        self.stats = StatsDisplay()
        self.border = Border()

    def tick(self, time: float):
        self.mpf.tick(time)
        self.stats.tick(time)
        self.border.tick(time)

    def render(self, player: PlayerState, playfield: Playfield, console: Crt):
        if self.stats.dirty:
            self.stats.render(player, console)
        if self.mpf.dirty:
            self.mpf.render(playfield, console)
        if self.border.dirty:
            self.border.render(self.mpf.rect.size, console)

    def mark_player_dirty(self):
        self.stats.stats_dirty = True

    def new_level(self, playfield: Playfield):
        self.mpf.new_level(playfield)
        self.border.new_level()
        self.stats.new_level()

    def new_border(self):
        self.border.new_level()

class MainPlayfield():
    def __init__(self, rect: Rect, gem_color: Color, visibility: VisibilityFlags, floor_colors: Optional[Tuple[Color, Color]] = None):
        self.dirty: bool = True
        self.rect = rect
        self.gem_color = gem_color
        self.visibility = visibility
        self.floor_colors = floor_colors
        self.blink_time = 0.0
        self.blink_on = True
        self.chanced: list[Tuple[int, int]] = []

    def tick(self, time: float):
        self.blink_time += time
        if self.blink_time > GameDisplay.BLINK_RATE:
            self.blink_time -= GameDisplay.BLINK_RATE
            self.blink_on = not self.blink_on

    def render(self, playfield: Playfield, console: Crt):
        if VisibilityFlags.HIDE_LEVEL in self.visibility:
            return
        if not self.dirty:
            return
        for x in range(self.rect.left, self.rect.right + 1):
            for y in range(self.rect.top, self.rect.bottom + 1):
                dr = draw(playfield[x, y], self.visibility)
                # HACK: Icky quirk = gem color and floor color are level-dependent
                if (playfield[x, y] is What.Nothing) and (self.floor_colors is not None):
                    console.print(x, y, dr.char, *self.floor_colors)
                elif playfield[x, y] is What.Gem:
                    console.print(x, y, dr.char, self.gem_color)
                else:
                    # TODO: Chance-ness for non-Chance Whats is state. So, to some extent, is invisibility
                    if (x, y) in self.chanced:
                        console.print(x, y, VisibleTiles.Chance, Colors.White)
                    elif (not self.blink_on) and dr.blinking:
                        console.print(x, y, ' ', dr.fg, dr.bg)
                    else:
                        console.print(x, y, dr.char, dr.fg, dr.bg)

    def new_level(self, playfield: Playfield):
        self.gem_color = Colors.RandomExcept([Colors.DarkGrey])
        self.dirty = True
        self.chanced = []
        for x in range(self.rect.left, self.rect.right + 1):
            for y in range(self.rect.top, self.rect.bottom + 1):
                chance = chance_of(playfield[x, y])
                if chance is not None:
                    if randrange(chance) == 0:
                        self.chanced.append(x, y)

class StatsDisplay():
    def __init__(self):
        self.stats_dirty: bool = True
        self.panel_dirty: bool = True
        self.gems_text = HudText('', Animation.NONE)

    @property
    def dirty(self):
        return self.stats_dirty or self.panel_dirty

    def tick(self, time):
        self.stats_dirty = self.stats_dirty or self.gems_text.tick(time)

    def render(self, player: PlayerState, console: Crt):
        if self.panel_dirty:
            console.window(66, 0, 79, 24)
            console.clrscr(Colors.Blue)
            console.window(0, 0, 79, 24)
            console.print(70, 0, 'Score', Colors.Yellow)
            console.print(70, 3, 'Level', Colors.Yellow)
            console.print(70, 6, 'Gems', Colors.Yellow)
            console.print(70, 9, 'Whips', Colors.Yellow)
            console.print(68, 12, 'Teleports', Colors.Yellow)
            console.print(70, 15, 'Keys', Colors.Yellow)
            console.print(69, 18, 'OPTIONS', Colors.LightCyan, Colors.Red)
            console.gotoxy(69, 19)
            console.write('W', Colors.White)
            console.write('hip', Colors.LightGrey)
            console.gotoxy(69, 20)
            console.write('T', Colors.White)
            console.write('eleport', Colors.LightGrey)
            console.gotoxy(69, 21)
            console.write('P', Colors.White)
            console.write('ause', Colors.LightGrey)
            console.gotoxy(69, 22)
            console.write('Q', Colors.White)
            console.write('uit', Colors.LightGrey)
            console.gotoxy(69, 23)
            console.write('S', Colors.White)
            console.write('ave', Colors.LightGrey)
            console.gotoxy(69, 24)
            console.write('R', Colors.White)
            console.write('estore', Colors.LightGrey)
        if self.stats_dirty:
            console.default_colors(Colors.Red, Colors.LightGrey)
            console.print(68, 1, f"{(player.score * 10):^7}")
            console.print(68, 4, f"{player.level:^7}")
            console.print(68, 7, f"{self.gems_text.message:^7}")
            if player.whip_power >= 3:
                s = f"{player.whips}+{player.whip_power}"
                console.print(68, 10, f"{s:^7}")
            else:
                console.print(68, 10, f"{player.whips:^7}")
            console.print(68, 13, f"{player.teleports:^7}")
            console.print(68, 16, f"{player.keys:^7}")

    def new_level(self):
        self.stats_dirty = True

class Border():
    def __init__(self):
        self.foreground: Color = Colors.Black
        self.background: Color = Colors.Black
        self.top_text: HudText = HudText('', Animation.NONE)
        self.bottom_text: HudText = HudText('', Animation.NONE)
        self.dirty: bool = True

    def tick(self, time: float):
        self.dirty = self.top_text.tick(time) or self.dirty
        self.dirty = self.bottom_text.tick(time) or self.dirty

    def render(self, containing_size: Tuple[int, int], console: Crt):
        if self.dirty:
            (width, height) = containing_size
            top_space = (width + 2 - len(self.top_text)) // 2
            bottom_space = (width + 2 - len(self.bottom_text)) // 2
            for x in range(top_space):
                console.print(x, 0, VisibleTiles.Breakable_Wall, self.foreground, self.background)
            console.print(top_space, 0, self.top_text.message,
                self.top_text.foreground if self.top_text.foreground is not None else self.foreground, self.background)
            for x in range(top_space):
                console.print(x + top_space + len(self.top_text), 0, VisibleTiles.Breakable_Wall, self.foreground, self.background)

            for y in range(1, height + 1):
                console.print(0, y, VisibleTiles.Breakable_Wall, self.foreground, self.background)
                console.print(width + 2, y, VisibleTiles.Breakable_Wall, self.foreground, self.background)

            for x in range(bottom_space):
                console.print(x, height + 2, VisibleTiles.Breakable_Wall, self.foreground, self.background)
            console.print(bottom_space, height + 2, self.bottom_text.message,
                self.bottom_text.foreground if self.bottom_text.foreground is not None else self.foreground, self.background)
            for x in range(bottom_space):
                console.print(x + bottom_space + len(self.bottom_text), 0, VisibleTiles.Breakable_Wall, self.foreground, self.background)

    def new_level(self):
        self.foreground = Colors.RandomLight()
        self.background = Colors.RandomDark()
        self.dirty = True

class Animation(Enum):
    NONE = 0
    BLINKING = 1
    RANDOM_COLOR = 2

class HudText():
    def __init__(self, message: str, animation: Animation, allowed_foreground_colors: Optional[list[Color]] = None):
        self.message = message
        self.foreground: Optional[Color] = None
        self.allowed_foreground_colors = allowed_foreground_colors if allowed_foreground_colors is not None else list(Colors.Code.values())
        self.animation = animation
        self.animation_time = 0.0
        self.animation_state_visible = True

    def __len__(self):
        return len(self.message) if self.animation_state_visible else 0

    def tick(self, time: float) -> bool:
        self.animation_time += time
        if self.animation is Animation.BLINKING:
            if self.animation_time > GameDisplay.BLINK_RATE:
                self.animation_time -= GameDisplay.BLINK_RATE
                self.animation_state_visible = not self.animation_state_visible
                return True
        elif self.animation is Animation.RANDOM_COLOR:
            if self.animation_time > GameDisplay.COLOR_RATE:
                self.animation_time -= GameDisplay.COLOR_RATE
                self.foreground = choice(self.allowed_foreground_colors)
                return True
        return False
