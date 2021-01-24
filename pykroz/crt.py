# Python Imports
from collections import deque
from sys import exit
from typing import  Optional, Union
from time import sleep
from enum import Enum

# Library Imports
import pygame
from pygame import Color, Rect
import pygame.locals
import pygame.display
import pygame.mixer
import pygame.key
from pygame.event import get
import numpy

# Project Imports
from ascii import ASCII
from colors import Colors, ContrastLevel
from sounds import SampleSet
from keyboard import Keyboard
from audio import Audio

class ColorMode(Enum):
    COLOR_PALLETTE = 1
    BLACK_AND_WHITE = 2

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
        self.current_window = Rect(1, 1, 80, 25)
        self.cursor_x = 0
        self.cursor_y = 0
        pygame.display.set_caption('PyKroz')
        self.size = widthInTiles, heightInTiles
        self.charbuffer: numpy.ndarray = numpy.zeros(self.size, dtype = 'i')
        self.fg_color_buffer: numpy.ndarray = numpy.zeros((*self.size, 3), dtype = 'i')
        self.bg_color_buffer: numpy.ndarray = numpy.zeros((*self.size, 3), dtype = 'i')
        self.dirty_blocks = deque([Rect(0, 0, *self.size)])
        self.color_mode: ColorMode = ColorMode.COLOR_PALLETTE

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
        while len(self.dirty_blocks) > 0:
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
        return self._keyboard.key_in_queue()

    def read(self) -> int:
        while not self._keyboard.key_in_queue():
            for event in get([
                pygame.locals.QUIT, 
                pygame.locals.KEYDOWN, 
                pygame.locals.KEYUP
            ], pump = True):
                if event.type == pygame.locals.QUIT:
                    exit()
                print(event)
                self._keyboard.handle(event)
        return self._keyboard.get_key_from_queue()

    def readkey(self) -> Optional[int]:
        return self._keyboard.get_key_from_queue()

    def readln(self) -> str:
        line = ''
        done = False
        while not done:
            for event in get([
                pygame.locals.QUIT, 
                pygame.locals.KEYDOWN, 
                pygame.locals.KEYUP
            ], pump = True):
                if event.type == pygame.locals.QUIT:
                    exit()
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key in [pygame.locals.K_ESCAPE, pygame.locals.K_RETURN, pygame.locals.K_KP_ENTER]:
                        done = True
                    elif event.key in [pygame.locals.K_BACKSPACE, pygame.locals.K_DELETE]:
                        line = line[:-1]
                        self.cursor_x -= 1
                        self.write(' ')
                        self.cursor_x -= 1
                    else:
                        line += event.unicode
                        self.write(event.unicode)
        return line

    def write(self, message: Union[str, int], fore: Optional[Color] = None, back: Optional[Color] = None):
        if not self.current_window.collidepoint(self.cursor_x, self.cursor_y):
            return
        fg = [*self.foreground[0:3]] if fore is None else [*fore[0:3]]
        bg = [*self.background[0:3]] if back is None else [*back[0:3]]
        if isinstance(str, message):
            clipped_message = message[0:(self.current_window.width - self.cursor_x)]
            self.dirty_blocks.append(Rect(self.cursor_x, self.cursor_y, len(clipped_message), 1))
            for c in range(len(clipped_message)):
                self.charbuffer[self.cursor_x + c, self.cursor_y] = ASCII.Ord[clipped_message[c]]
                self.fg_color_buffer[self.cursor_x + c, self.cursor_y] = fg
                self.bg_color_buffer[self.cursor_x + c, self.cursor_y] = bg
            self.cursor_x += len(clipped_message)
        else:
            self.charbuffer[self.cursor_x, self.cursor_y] = message
            self.fg_color_buffer[self.cursor_x, self.cursor_y] = fg
            self.bg_color_buffer[self.cursor_x, self.cursor_y] = bg
            self.cursor_x += 1

    def writeln(self, message: Union[str, None] = None, fore: Optional[Color] = None, back: Optional[Color] = None):
        if message is not None:
            self.write(message, fore, back)
        self.cursor_x = 0
        self.cursor_y += 1

    def print(self, XPos: int, YPos: int, Message: str, fore: Optional[Color] = None, back: Optional[Color] = None):
        self.cursor_x = XPos
        self.cursor_y = YPos
        self.write(Message, fore, back)

    def window(self, x_min: int, y_min: int, x_max: int, y_max: int):
        self.current_window = Rect(x_min, y_min, x_max - x_min, y_max - y_min)

    def gotoxy(self, x: int, y: int):
        self.cursor_x = x
        self.cursor_y = y

    def delay(self, ms: int):
        sleep(ms / 1000)

    def reset_colors(self):
        self.foreground = Colors.White
        self.background = Colors.Black

    def default_colors(self, fore: Union[int, Color, None] = None, back: Union[int, Color, None] = None, contrast: Optional[ContrastLevel] = None):
        def translate_color(color: Union[int, Color]) -> Color:
            if isinstance(color, int):
                mod_color = color % len(Colors.Code) # I think colors beyond 15 are meant to blink
                if self.color_mode == ColorMode.COLOR_PALLETTE:
                    return Colors.Code[mod_color]
                else:
                    if mod_color in [0, 7, 8, 15]: # Already greyscale
                        return Colors.Code[mod_color]
                    elif mod_color in [1, 3]: # Very dark shades
                        return Colors.Black
                    elif mod_color in [2, 4, 5, 6]: # Dark Shades
                        return Colors.DarkGrey
                    elif mod_color in [9, 10, 11, 13]: # Light Shades
                        return Colors.LightGrey
                    elif mod_color in [12, 14]: # Very light colors
                        return Colors.White
            else:
                return color
        if fore is not None:
            self.foreground = translate_color(fore)
        if back is not None:
            self.background = translate_color(back)

    def sound(self, freq: int, duration: int):
        self._audio.sound(self._audio.tone(freq, duration, self._audio.square_wave))

    def sounds(self, parts: SampleSet):
        self._audio.sound(self._audio.compose(parts))

    def clrscr(self, color: Optional[Color]):
        fg = [*self.foreground[0:3]]
        bg = [*self.background[0:3]] if color is None else [*color[0:3]]
        for x in range(self.current_window.left, self.current_window.left + self.current_window.width):
            for y in range(self.current_window.top, self.current_window.top + self.current_window.height):
                self.charbuffer[x, y] = ' '
                self.fg_color_buffer[x, y] = fg
                self.bg_color_buffer[x, y] = bg
        self.dirty_blocks.append(self.current_window)

    def clearkeys(self):
        self._keyboard.clear_queue()

    def halt(self):
        exit()

    def insline(self):
        pass

    def delline(self):
        pass