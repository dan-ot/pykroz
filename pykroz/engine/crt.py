# Python Imports
from collections import deque
from typing import  Optional, Union
from time import sleep
from enum import Enum
import sys

# Library Imports
import pygame
from pygame import Color, Rect
import pygame.constants
import pygame.display
import pygame.mixer
import pygame.key
from pygame.event import get
import numpy

# Project Imports
from engine.ascii import ASCII
from engine.colors import Colors
from engine.audio import SampleSet, Audio
from engine.keyboard import Keyboard
from levels import VisibleTiles, XBOT, XSIZE, YBOT, YTOP

class ColorMode(Enum):
    COLOR_PALLETTE = 1
    BLACK_AND_WHITE = 2

class Crt:
    def __init__(self, widthInTiles: int, heightInTiles: int, fontFile: Union[str, None]):
        (frequency, bit_depth, _) = pygame.mixer.get_init()
        self._audio = Audio(frequency, bit_depth)

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
            pygame.constants.QUIT,
            pygame.constants.KEYDOWN,
            pygame.constants.KEYUP
        ], pump = True):
            if event.type == pygame.constants.QUIT:
                sys.exit()
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
            self.tick()
        key = self._keyboard.get_key_from_queue()
        return key if key is not None else 0

    def readkey(self) -> Optional[int]:
        return self._keyboard.get_key_from_queue()

    def readln(self) -> str:
        line = ''
        done = False
        while not done:
            for event in get([
                pygame.constants.QUIT,
                pygame.constants.KEYDOWN,
                pygame.constants.KEYUP
            ], pump = True):
                if event.type == pygame.constants.QUIT:
                    exit()
                elif event.type == pygame.constants.KEYDOWN:
                    if event.key in [pygame.constants.K_ESCAPE, pygame.constants.K_RETURN, pygame.constants.K_KP_ENTER]:
                        done = True
                    elif event.key in [pygame.constants.K_BACKSPACE, pygame.constants.K_DELETE]:
                        line = line[:-1]
                        self.cursor_x -= 1
                        self.write(' ')
                        self.cursor_x -= 1
                    else:
                        line += event.unicode
                        self.write(event.unicode)
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
        return line

    def write(self, message: Union[str, int], fore: Optional[Color] = None, back: Optional[Color] = None):
        if not self.current_window.collidepoint(self.cursor_x, self.cursor_y):
            return
        fg = [*self.foreground[0:3]] if fore is None else [*fore[0:3]]
        bg = [*self.background[0:3]] if back is None else [*back[0:3]]
        if isinstance(message, str):
            clipped_message = message[0:(self.current_window.width - self.cursor_x)]
            self.dirty_blocks.append(Rect(self.cursor_x, self.cursor_y, len(clipped_message), 1))
            for (i, c) in enumerate(clipped_message):
                self.charbuffer[self.cursor_x + i, self.cursor_y] = ASCII.Ord[c]
                self.fg_color_buffer[self.cursor_x + i, self.cursor_y] = fg
                self.bg_color_buffer[self.cursor_x + i, self.cursor_y] = bg
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

    def alert(self, YPos: int, Message: str, bc: Color, bb: Color):
        colors = [Colors.Yellow, Colors.White]
        left = (XSIZE - len(Message)) // 2 # Half the empty space needed to show the message
        counter = 0
        while not self.keypressed():
            counter = (counter + 1) % 2
            self.delay(20)
            self.print(left, YPos, Message, colors[counter], Colors.Black)
            self.tick() # keep the message pump and frame rate alive...
        if YPos == YTOP + 1: # Bottom border alert
            self.gotoxy(XBOT - 1, YTOP + 1)
            for _ in range(XSIZE + 1):
                self.write(VisibleTiles.Breakable_Wall, bc, bb)
        elif YPos == YBOT - 1: # Top border alert
            self.gotoxy(XBOT - 1, YBOT - 1)
            for _ in range(XSIZE + 1):
                self.write(VisibleTiles.Breakable_Wall, bc, bb)


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

    def default_colors(self, fore: Optional[Color] = None, back: Optional[Color] = None):
        # def translate_color(color: Union[int, Color]) -> Color:
        #     if isinstance(color, int):
        #         mod_color = color % len(Colors.Code) # I think colors beyond 15 are meant to blink
        #         if self.color_mode == ColorMode.COLOR_PALLETTE:
        #             return Colors.Code[mod_color]
        #         else:
        #             if mod_color in [0, 7, 8, 15]: # Already greyscale
        #                 return Colors.Code[mod_color]
        #             elif mod_color in [1, 3]: # Very dark shades
        #                 return Colors.Black
        #             elif mod_color in [2, 4, 5, 6]: # Dark Shades
        #                 return Colors.DarkGrey
        #             elif mod_color in [9, 10, 11, 13]: # Light Shades
        #                 return Colors.LightGrey
        #             elif mod_color in [12, 14]: # Very light colors
        #                 return Colors.White
        #     else:
        #         return color
        if fore is not None:
            self.foreground = fore
        if back is not None:
            self.background = back

    def sound(self, freq: int, duration: float):
        self._audio.sound(self._audio.tone(freq, duration, self._audio.square_wave))

    def sounds(self, parts: SampleSet):
        self._audio.sound(self._audio.compose(parts, self._audio.square_wave))

    def clrscr(self, color: Optional[Color] = None):
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
