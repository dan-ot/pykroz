# Python Imports
from collections import deque
from sys import exit

# Library Imports
import pygame
from pygame.freetype import Font
import pygame.locals
import pygame.display
import pygame.time
from pygame.key import set_repeat
from pygame.event import get, Event
import numpy

# Project Imports
from tiles import Tiles
from colors import Colors

class Keyboard():
    def __init__(self):
        self.keyboard = {}
        self.keys = deque()

    def dispatch(self, event: Event):
        if event.type == pygame.locals.KEYDOWN:
            self.keyboard[event.key] = True
            self.keys.appendleft(event.key)
        elif event.type == pygame.locals.KEYUP:
            self.keyboard[event.key] = False
        elif event.type == pygame.locals.QUIT:
            exit()

    def getKey(self):
        return self.keys.pop()

    def clear(self):
        self.keys.clear()

    def keypressed(self):
        return self.keys.count() > 0

class Crt:
    def __init__(self, widthInTiles: int, heightInTiles: int, fontFile: str, fontPointSize: int, zoom: float):
        font = Font(fontFile)
        font.size = fontPointSize
        self.tileRect = font.get_rect('W')
        self.font = font
        self.keyboard = Keyboard()
        self.foreground = Colors.White
        self.background = Colors.Black
        self.screen = pygame.display.set_mode((int(self.tileRect.width * widthInTiles * zoom), int(self.tileRect.height * heightInTiles * zoom)))
        self.clock = pygame.time.Clock()
        self.charbuffer = numpy.zeros((widthInTiles, heightInTiles), dtype = 'U1')
        self.charbuffer.fill(Tiles.Code[2])
        self.fg_color_buffer = numpy.zeros((widthInTiles, heightInTiles, 3), dtype = 'i')
        self.fg_color_buffer.fill(255)
        self.bg_color_buffer = numpy.zeros((widthInTiles, heightInTiles, 3), dtype = 'i')
        self.zoom = zoom

    def open(self):
        # set_blocked([pygame.locals.MOUSEBUTTONDOWN, pygame.locals.MOUSEBUTTONUP, pygame.locals.MOUSEMOTION, pygame.locals.MOUSEWHEEL, pygame.locals.WINDOWENTER, pygame.locals.WINDOWLEAVE])
        set_repeat(0)
        print(self.tileRect)
        while True:
            self.clock.tick(30)
            for event in get([pygame.locals.QUIT, pygame.locals.KEYDOWN, pygame.locals.KEYUP], pump = True):
                print(event)
                self.keyboard.dispatch(event)
            for tx in range(len(self.charbuffer)):
                for ty in range(len(self.charbuffer[tx])):
                    self.font.render_to(
                        self.screen, 
                        (tx * self.tileRect.width * self.zoom, ty * self.tileRect.height * self.zoom),
                        self.charbuffer[tx, ty],
                        self.fg_color_buffer[tx, ty],
                        self.bg_color_buffer[tx, ty]
                    )

            pygame.display.flip()