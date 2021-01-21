# Python Imports
from audio import Audio
from collections import deque
from sys import exit
from typing import  Union
from time import sleep

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
from ascii import ASCII
from colors import Colors
from sounds import SampleSet

class Keyboard():
    def __init__(self):
        self.keyboard = {}
        self.keys: deque[int] = deque()
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
        self._audio = Audio(frequency, format)

        if fontFile is None:
            tiles = ASCII.from_system_font() 
        elif fontFile.endswith('.ttf'):
            tiles = ASCII.from_font_file(fontFile)
        else:
            tiles = ASCII.from_bitmap_font(fontFile, (8, 12))
        
        self._tiles = tiles
        self._screen = pygame.display.set_mode((self._tiles.width * widthInTiles, self._tiles.height * heightInTiles))
        self._keyboard = Keyboard()
        self.foreground = Colors.White
        self.background = Colors.Black
        self.cursor_x = 0
        self.cursor_y = 0
        pygame.display.set_caption('PyKroz')
        self.size = widthInTiles, heightInTiles
        self.charbuffer: numpy.ndarray = numpy.zeros(self.size, dtype = 'i')
        self.fg_color_buffer: numpy.ndarray = numpy.zeros((*self.size, 3), dtype = 'i')
        self.bg_color_buffer: numpy.ndarray = numpy.zeros((*self.size, 3), dtype = 'i')
        self.dirty_blocks = deque([Rect(0, 0, *self.size)])

    def tick(self):
        for event in get([
            pygame.locals.QUIT, 
            pygame.locals.KEYDOWN, 
            pygame.locals.KEYUP
        ], pump = True):
            if event.type == pygame.locals.QUIT:
                exit()
            print(event)
            self._keyboard.handle(event)
        self._audio.tick()
        for _ in range(len(self.dirty_blocks)):
            dirty = self.dirty_blocks.popleft()
            for x in range(dirty.width):
                for y in range(dirty.height):
                    tx = x + dirty.left
                    ty = y + dirty.top
                    self._tiles.draw(
                        self.charbuffer[tx, ty],
                        tx * self._tiles.width, ty * self._tiles.height,
                        pygame.Color(self.fg_color_buffer[tx, ty]),
                        pygame.Color(self.bg_color_buffer[tx, ty]),
                        self._screen
                    )

        pygame.display.flip()

    def keypressed(self) -> bool:
        return self._keyboard.keypressed()

    def read(self) -> int:
        pass

    def readkey(self):
        return self._keyboard.getKey()

    def write(self, message: Union[str, int]):
        if isinstance(str, message):
            self.dirty_blocks.append(Rect(self.cursor_x, self.cursor_y, len(message), 1))
            for c in range(len(message)):
                self.charbuffer[self.cursor_x + c, self.cursor_y] = ASCII.Ord[message[c]]
                self.fg_color_buffer[self.cursor_x + c, self.cursor_y] = self.foreground
                self.bg_color_buffer[self.cursor_x + c, self.cursor_y] = self.background
            self.cursor_x += len(message)
        else:
            self.charbuffer[self.cursor_x, self.cursor_y] = message
            self.fg_color_buffer[self.cursor_x, self.cursor_y] = self.foreground
            self.bg_color_buffer[self.cursor_x, self.cursor_y] = self.background
            self.cursor_x += 1

    def writeln(self, message: Union[str, None] = None):
        if message is not None:
            self.write(message)
        self.cursor_x = 0
        self.cursor_y += 1

    def window(self, x_min: int, y_min: int, x_max: int, y_max: int):
        pass

    def gotoxy(self, x: int, y: int):
        self.cursor_x = x
        self.cursor_y = y

    def delay(ms: int):
        sleep(ms / 1000)

    def textcolor(self, index: int):
        self.foreground = Colors.Code[index % len(Colors.Code)]

    def textbackground(self, index: int):
        self.background = Colors.Code[index % len(Colors.Code)]

    def sound(self, freq: int, duration: int):
        self._audio.sound(self._audio.tone(freq, duration, self._audio.square_wave))

    def sounds(self, parts: SampleSet):
        self._audio.sound(self._audio.compose(parts))

    def clrscr(self):
        self.charbuffer.fill(ASCII.Ord[' '])
        self.fg_color_buffer.fill(255)
        self.bg_color_buffer.fill(0)
        self.dirty_blocks.append(Rect(0, 0, *self.size))

    def halt(self):
        exit()

    def insline(self):
        pass

    def delline(self):
        pass