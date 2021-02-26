from pygame import Rect, Surface

from states.protocols import CommandableState
from commands import Command
from engine.ascii import ASCII

class MenuState():
    def __init__(self, initialState, font: ASCII, size: Rect):
        self.state = initialState


    def tick(self, deltaTime: float) -> CommandableState:
        return self #.state.tick(deltaTime)

    def render(self, surface: Surface) -> None:
        pass
        #self.state.render(surface)

    def command(self, command: Command):
        pass
