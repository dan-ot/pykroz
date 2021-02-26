from pygame import Rect
from pygame.display import set_mode, set_caption, flip
from pygame.time import Clock
from pygame.event import get
from pygame.joystick import Joystick
import pygame.constants

from engine.ascii import ASCII
from engine.keyboard import Keyboard
from states.menu_state import MenuState
from states.protocols import CommandableState
from commands import command_from_button, command_from_hat, command_from_key_code

class CoreState():
    def __init__(self):
        self._clock = Clock()
        self._keyboard = Keyboard()
        self._joystick = Joystick(0)
        self._joystick.init()
        self._font = ASCII.from_bitmap_font('assets/terminal8x12_gs_ro.png', (8, 12))
        self._state: CommandableState = MenuState(None, self._font, Rect(0, 0, 80, 25))
        self._screen = set_mode((self._font.width * 80, self._font.height * 25))
        set_caption('PyKroz')

    def run(self):
        while True:
            delta = self._clock.tick(30)
            self._state = self._state.tick(delta)
            self._state.render(self._screen)

            for event in get([
                pygame.constants.QUIT,
                pygame.constants.KEYDOWN,
                pygame.constants.JOYHATMOTION,
                pygame.constants.JOYBUTTONDOWN
            ], pump = True):
                if event.type is pygame.constants.QUIT:
                    exit()

                if event.type == pygame.constants.KEYDOWN:
                    command = command_from_key_code(event.key)
                    if command is not None:
                        self._state.command(command)

                if event.type == pygame.constants.JOYHATMOTION:
                    command = command_from_hat(event.value)
                    if command is not None:
                        self._state.command(command)

                if event.type == pygame.constants.JOYBUTTONDOWN:
                    command = command_from_button(event.button)
                    if command is not None:
                        self._state.command(command)

            flip()
