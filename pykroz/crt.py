from collections import deque
from typing import cast
import tcod
import pygame.freetype
from tcod.console import Console
from tcod.context import new
from tcod.event import Event, KeyUp, get, wait, KeyDown, Quit
from tcod.tileset import CHARMAP_CP437, load_tilesheet

class Keyboard(tcod.event.EventDispatch):
    def __init__(self):
        self.keyboard = {}
        self.keys = deque()

    def ev_keydown(self, event: KeyDown):
        if not event.repeat:
            self.keyboard[event.sym] = True
            self.keys.appendleft(event.sym)

    def ev_keyup(self, event: KeyUp):
        self.keyboard[event.sym] = False

    def ev_quit(self, event: Quit):
        raise SystemExit()

    def getKey(self):
        return self.keys.pop()

    def lastKey(self):
        key = self.keys.popleft()
        self.keys.clear()
        return key

class Tiles:
    def __init__(self, file: str):
        self.font = pygame.freetype.Font(file)

class Crt:
    def __init__(self, width: int, height: int, tiles: str):
        tileset = load_tilesheet(tiles, 16, 16, CHARMAP_CP437)
        self.console = Console(width, height, order="F")
        self.context = new(columns = self.console.width, rows = self.console.height, tileset = tileset)
        self.console.clear()
        self.keypressed = False
        self.keyboard = Keyboard()

    def __del__(self):
        self.context.close()

    def open(self):
        while True:
            tcod.sys_set_fps(30)
            tcod.console_flush()
            self.context.present(self.console)
            for ev in get():
                event = cast(Event, ev)
                self.keyboard.dispatch(event)