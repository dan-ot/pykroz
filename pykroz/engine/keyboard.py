from collections import deque
from typing import Optional

import pygame.locals
import pygame.key
from pygame.event import Event

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

    def get_key_from_queue(self) -> Optional[int]:
        if len(self.keys) > 0:
            return self.keys.pop()
        else:
            return None

    def clear_queue(self):
        self.keys.clear()

    def key_in_queue(self):
        return len(self.keys) > 0