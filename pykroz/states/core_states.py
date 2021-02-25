from engine.ascii import ASCII
from typing import Protocol

from pygame import Rect, Surface
from pygame.display import set_mode, flip
from pygame.time import Clock

from engine.crt import Crt
from levels import Game
from states.menu_state import MenuState

class TickableState(Protocol):
    def tick(self, deltaTime: float) -> 'TickableState':
        ...

    def render(self, surface: Surface) -> None:
        ...

class CoreState():
    def __init__(self):
        self._clock = Clock()
        self._font = ASCII.from_bitmap_font('assets/terminal8x12_gs_ro.png', (8, 12))
        self._state: TickableState = MenuState(None, self._font, Rect(0, 0, 80, 25))
        self._screen = set_mode((self._font.width * 80, self._font.height * 25))

    def run(self):
        while True:
            delta = self._clock.tick(30)
            self._state = self._state.tick(delta)
            self._state.render(self._screen)

            flip()
