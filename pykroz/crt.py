# Python Imports
from audio import Audio
from collections import deque
from sys import exit
from random import randint
from typing import Sequence, Tuple, Union

# Library Imports
import pygame
from pygame import Rect
import pygame.locals
import pygame.display
import pygame.mixer
import  pygame.key
from pygame.event import get, Event
import numpy

# Project Imports
from tiles import Tiles
from colors import Colors

class Keyboard():
    def __init__(self):
        self.keyboard = {}
        self.keys = deque()
        pygame.key.set_repeat(0)

    def handle(self, event: Event):
        if event.type == pygame.locals.KEYDOWN:
            self.keyboard[event.key] = True
            self.keys.appendleft(event.key)
        elif event.type == pygame.locals.KEYUP:
            self.keyboard[event.key] = False

    def getKey(self):
        return self.keys.pop()

    def clear(self):
        self.keys.clear()

    def keypressed(self):
        return self.keys.count() > 0

class Crt:
    def __init__(self, widthInTiles: int, heightInTiles: int, fontFile: Union[str, None]):
        (frequency, format, _) = pygame.mixer.get_init()
        self.audio = Audio(frequency, format)

        if fontFile is None:
            tiles = Tiles.from_system_font() 
        elif fontFile.endswith('.ttf'):
            tiles = Tiles.from_font_file(fontFile)
        else:
            tiles = Tiles.from_bitmap_font(fontFile, (8, 12))
        
        self.tiles = tiles
        self.screen = pygame.display.set_mode((self.tiles.width * widthInTiles, self.tiles.height * heightInTiles))
        self.keyboard = Keyboard()
        self.foreground = Colors.White
        self.background = Colors.Black
        self.cursor_x = 0
        self.cursor_y = 0
        pygame.display.set_caption('PyKroz')
        self.charbuffer = numpy.zeros((widthInTiles, heightInTiles), dtype = 'i')
        # self.charbuffer = numpy.array([[randint(0, 255) for y in range(heightInTiles)] for x in range(widthInTiles)])
        self.fg_color_buffer = numpy.zeros((widthInTiles, heightInTiles, 3), dtype = 'i')
        # self.fg_color_buffer = numpy.array([[[randint(0, 255), randint(0, 255), randint(0, 255)] for y in range(heightInTiles)] for x in range(widthInTiles)])
        self.bg_color_buffer = numpy.zeros((widthInTiles, heightInTiles, 3), dtype = 'i')
        self.dirty_blocks = deque([Rect(0, 0, widthInTiles, heightInTiles)])

    def tick(self):
        for event in get([
            pygame.locals.QUIT, 
            pygame.locals.KEYDOWN, 
            pygame.locals.KEYUP
        ], pump = True):
            if event.type == pygame.locals.QUIT:
                exit()
            print(event)
            self.keyboard.handle(event)
        self.audio.tick()
        for _ in range(len(self.dirty_blocks)):
            dirty = self.dirty_blocks.popleft()
            for x in range(dirty.width):
                for y in range(dirty.height):
                    tx = x + dirty.left
                    ty = y + dirty.top
                    self.tiles.draw(
                        self.charbuffer[tx, ty],
                        tx * self.tiles.width, ty * self.tiles.height,
                        pygame.Color(self.fg_color_buffer[tx, ty]),
                        pygame.Color(self.bg_color_buffer[tx, ty]),
                        self.screen
                    )

        pygame.display.flip()

    def keypressed(self) -> bool:
        return self.keyboard.keypressed()

    def readkey(self):
        return self.keyboard.getKey()

    def write(self, message: str):
        self.dirty_blocks.append(Rect(self.cursor_x, self.cursor_y, len(message), 1))
        for c in range(len(message)):
            self.charbuffer[self.cursor_x + c, self.cursor_y] = Tiles.Value[message[c]]
            self.fg_color_buffer[self.cursor_x + c, self.cursor_y] = self.foreground
            self.bg_color_buffer[self.cursor_x + c, self.cursor_y] = self.background
        self.cursor_x += len(message)

    def gotoxy(self, x: int, y: int):
        self.cursor_x = x
        self.cursor_y = y

    def textcolor(self, index: int):
        self.foreground = Colors.Code[index % len(Colors.Code)]

    def textbackground(self, index: int):
        self.background = Colors.Code[index % len(Colors.Code)]

    def sound(self, freq: int, duration: int):
        self.audio.sound(freq, duration)

    def sounds(self, parts: Sequence[Tuple[int, int]]):
        self.audio.compose(parts)