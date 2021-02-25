from pygame import Surface

from states.core_states import TickableState

class PlayState():
    def tick(self, deltaTime: float) -> TickableState:
        return self

    def render(self, surface: Surface) -> None:
        pass
