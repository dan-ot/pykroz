from pygame import Rect, Surface

from states.core_states import TickableState
from engine.ascii import ASCII

class MenuState():
    def __init__(self, initialState: TickableState, font: ASCII, size: Rect):
        self.state = initialState


    def tick(self, deltaTime: float) -> TickableState:
        return self.state.tick(deltaTime)

    def render(self, surface: Surface) -> None:
        self.state.render(surface)
